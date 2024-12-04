from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

class OpenAiModel():

    def __init__(self,model_name,key,temperature=0.5):
        self.model = ChatOpenAI(temperature=temperature,model_name = model_name,openai_api_key=key)

    def talk_to_model(self,system_message,human_message):
        messages = [
            system_message,
            human_message
        ]
        return self.model(messages).content