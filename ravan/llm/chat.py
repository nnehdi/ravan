import os

from dotenv import find_dotenv, load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory


class Chat:
    def __init__(self, system_prompt) -> None:
        load_dotenv(find_dotenv())
        self.llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.system_prompt = system_prompt
        self.history = ChatMessageHistory()
        self.history.add_ai_message(self.system_prompt)

    def chat(self, message=None):
        if message:
            self.history.add_user_message(message)
        response = self.llm(self.history.messages)
        self.history.add_ai_message(response.content)
        return response.content
