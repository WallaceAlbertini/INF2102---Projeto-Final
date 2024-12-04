from data_loader import DataLoader
from model import OpenAiModel
from pre_processor import PreProcessor
from prompter import Prompter
from retriever import Retriever
import re


class Controller:
    """
    Classe responsável por coordenar o fluxo de dados entre diferentes módulos:
    - Carregamento de dados
    - Pré-processamento
    - Recuperação de documentos relevantes
    - Consulta a um modelo de linguagem
    """
    def __init__(self, embedding_model, model_name, key, file_name, list_of_sheets) -> None:
        """
        Inicializa o controlador configurando os componentes principais.

        Args:
            embedding_model (str): Modelo usado para gerar embeddings.
            model_name (str): Nome do modelo de linguagem utilizado.
            key (str): Chave de API para o modelo de linguagem.
            file_name (str): Nome do arquivo Excel a ser carregado.
            list_of_sheets (list): Lista de abas a serem carregadas no DataFrame.
        """
        # Inicializa os módulos
        self.loader = DataLoader()  # Carregador de dados
        self.prompter = Prompter()  # Gerenciador de prompts
        self.preprocessor = PreProcessor(embedding_model)  # Pré-processador de texto
        self.retriever = Retriever()  # Mecanismo de recuperação baseado em vetores
        self.model = OpenAiModel(model_name=model_name, key=key)  # Modelo de linguagem
   
        # Carrega e pré-processa os dados
        df = self.loader.load_excel(file_name, list_of_sheets)
        df = self.preprocessor.preprocess(df)
        
        # Configura o armazenamento vetorial no Retriever
        self.retriever.set_vector_storage(df)
        
    def run(self, query):
        """
        Executa uma consulta ao sistema RAG (Retriever-Augmented Generation).
        
        Args:
            query (str): Consulta fornecida pelo usuário.

        Returns:
            str: Resposta do modelo para a consulta.
        """
        # Recupera os resultados mais relevantes
        closest_results = self.retriever.get_k_closest(
            self.preprocessor.encode_single(query), query, 10
        )
        print("\nPara a query: ", query, "\n\n")

        # Gera a resposta do modelo com base nos resultados recuperados
        model_response = self.model.talk_to_model(
            self.prompter.get_system_message(closest_results),
            self.prompter.get_human_message(query)
        )
        print("Resposta do modelo: \n", model_response)
        return model_response

    def run_1_shot(self, query):
        """
        Executa uma consulta em modo 1-shot (com apenas um exemplo no prompt).

        Args:
            query (str): Consulta fornecida pelo usuário.

        Returns:
            str: Resposta do modelo para a consulta.
        """
        # Gera a resposta do modelo usando mensagens específicas para 1-shot
        model_response = self.model.talk_to_model(
            self.prompter.get_system_message_1_shot(),
            self.prompter.get_human_message(query)
        )
        print("Resposta do modelo: \n", model_response)
        return model_response

    def get_y_pred_rag(self):
        """
        Gera as previsões do modelo usando o fluxo RAG.

        Returns:
            list: Lista de previsões extraídas das respostas do modelo.
        """
        df = self.loader.get_df()
        y_pred = []

        # Itera sobre o DataFrame, processando cada linha
        for _, row in df.iterrows():
            result = self.run(row['Quote'])  # Executa a consulta no modelo
            match = re.search(r'\*\*(.*?)\*\*', result)  # Extrai o texto entre "**"
            if match:
                y = match.group(1)
                y_pred.append(y)
                print("\n Adicionei na lista y:\n", y)
        return y_pred

    def get_y_pred_1_shot(self):
        """
        Gera as previsões do modelo usando o fluxo 1-shot.

        Returns:
            list: Lista de previsões extraídas das respostas do modelo.
        """
        df = self.loader.get_df()
        y_pred = []

        # Itera sobre o DataFrame, processando cada linha
        for _, row in df.iterrows():
            result = self.run_1_shot(row['Quote'])  # Executa a consulta no modelo
            match = re.search(r'\*\*(.*?)\*\*', result)  # Extrai o texto entre "**"
            if match:
                y = match.group(1)
                y_pred.append(y)
        return y_pred

    def get_data_loader(self):
        """
        Retorna o objeto de carregamento de dados.

        Returns:
            DataLoader: Objeto DataLoader utilizado pelo controlador.
        """
        return self.loader
