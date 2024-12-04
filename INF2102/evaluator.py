from sklearn.metrics import f1_score, accuracy_score



class Evaluator:
    """
    Classe para avaliar o desempenho do sistema em tarefas de classificação.
    Utiliza métricas como F1-score e accuracy para comparar previsões com valores reais.
    """

    def __init__(self, controller) -> None:
        """
        Inicializa a classe com uma instância do Controller.

        Args:
            controller (Controller): Objeto controlador que realiza as previsões.
        """
        self.controller = controller

    def calculate_f1_score_rag(self):
        """
        Calcula o F1-score (macro) para o sistema RAG.

        Returns:
            float: F1-score (macro) das previsões RAG.
        """
        # Obtenção dos valores reais (y_true) e previsões (y_pred)
        data_loader = self.controller.get_data_loader()
        y_true = data_loader.get_y_true()
        print("Valores reais (y_true):\n", y_true)

        y_pred = self.controller.get_y_pred_rag()
        print("Previsões (y_pred):\n", y_pred)

        # Retorna o F1-score com média macro
        return f1_score(y_true, y_pred, average='macro')

    def calculate_f1_score_1_shot(self):
        """
        Calcula o F1-score (macro) para o sistema em modo 1-shot.

        Returns:
            float: F1-score (macro) das previsões 1-shot.
        """
        data_loader = self.controller.get_data_loader()
        y_true = data_loader.get_y_true()
        print("Valores reais (y_true):\n", y_true)

        y_pred = self.controller.get_y_pred_1_shot()
        print("Previsões (y_pred):\n", y_pred)

        return f1_score(y_true, y_pred, average='macro')

    def evaluate_rag(self):
        """
        Avalia o desempenho do sistema RAG, retornando a acurácia.

        Returns:
            float: Acurácia das previsões RAG.
        """

        # Obtenção dos valores reais (y_true) e previsões (y_pred)
        data_loader = self.controller.get_data_loader()
        y_true = data_loader.get_y_true()
        print("Valores reais (y_true):\n", y_true)

        y_pred = self.controller.get_y_pred_rag()
        print("Previsões (y_pred):\n", y_pred)

        # Calcula e retorna a acurácia
        return accuracy_score(y_true, y_pred)

    def evaluate_1_shot(self):
        """
        Avalia o desempenho do sistema em modo 1-shot, retornando a acurácia e o F1-score.

        Returns:
            tuple: Acurácia e F1-score (macro) das previsões 1-shot.
        """
        data_loader = self.controller.get_data_loader()
        y_true = data_loader.get_y_true()
        print("Valores reais (y_true):\n", y_true)

        y_pred = self.controller.get_y_pred_1_shot()
        print("Previsões (y_pred):\n", y_pred)

        # Retorna a acurácia e o F1-score
        return accuracy_score(y_true, y_pred), f1_score(y_true, y_pred, average='macro')
