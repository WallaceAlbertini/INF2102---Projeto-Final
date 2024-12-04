from controller import Controller
# from evaluator import Evaluator
from view import View


openai_api_key= "SUA CHAVE DE API AQUI"
model_name = "gpt-4o-mini"
embedding_model = 'all-MiniLM-L6-v2'
file_name = 'Análise Temática de Conteúdo.xlsx'
list_of_sheets = ["SUA LISTA DE PLANILHAS AQUI"]


controller = Controller(embedding_model,model_name,openai_api_key,file_name,list_of_sheets)
# evaluator = Evaluator(controller)
#print(evaluator.evaluate_rag())
#print(controller.run("O que é o ensino?"))

view = View(controller)

view.run()

    