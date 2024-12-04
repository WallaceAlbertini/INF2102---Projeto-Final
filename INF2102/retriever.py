import chromadb
from data_loader import DataLoader
from model import OpenAiModel
from pre_processor import PreProcessor
from prompter import Prompter


class Retriever:
    """
    Classe responsável pela gestão e recuperação de dados vetorizados utilizando ChromaDB.
    """


    def __init__(self) -> None:
        """
        Inicializa a classe Retriever com uma conexão ao cliente ChromaDB
        e cria ou obtém uma coleção chamada 'interviews_sentiment'.
        """
        client = chromadb.Client()
        self.collection = client.get_or_create_collection(name="interviews_sentiment")

    def set_vector_storage(self, df):
        """
        Armazena embeddings e metadados no ChromaDB.

        Args:
            df (pd.DataFrame): DataFrame contendo colunas 'Embeddings', 'Quote' e 'Categoria'.
        """
        
        for i, row in df.iterrows():
            
            embedding = row['Embeddings']
            quote = row['Quote']
            categoria = row['Categoria']
            try:
            # Adiciona o embedding e os metadados à coleção
                self.collection.add(
                    ids=str(i),  # IDs devem ser strings únicas
                    embeddings=embedding,  # Vetores embasados no modelo
                    metadatas={"categoria": categoria, "quote": quote},  # Metadados adicionais
                )
            except Exception as e:
                print(f"Erro ao adicionar o vetor {i}: {e}")

    def get_k_closest(self, query_embbed, query, k=5):
        """
        Recupera os K vetores mais próximos de um embedding de consulta.

        Args:
            query_embbed (list): Embedding da consulta.
            query (str): Texto da consulta.
            k (int, opcional): Número de resultados a retornar. O padrão é 5.

        Returns:
            list: Lista de dicionários contendo os metadados dos resultados mais próximos.
        """
        # Realiza a consulta no ChromaDB
        results = self.collection.query(
            query_embeddings=[query_embbed],  # Embedding da consulta
            n_results=k  # Número de resultados a retornar
        )

        dict_results = []
        # Filtra os resultados para remover aqueles com o mesmo 'quote' que a consulta
        for result in results['metadatas'][0]:
            if result['quote'] != query:  # Evita incluir o próprio texto da consulta nos resultados
                dict_results.append(result)
        
        return dict_results
