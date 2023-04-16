# -*- coding: utf-8 -*-

import logging
import chatbotapiv2
from chatterbot import ChatBot


class MusharingChatbotConfig(chatbotapiv2.ChatbotConfig):
    """no config needed"""
    pass


class MusharingChatbot(chatbotapiv2.Chatbot):
    """MusharingChatbot is a Chatbot implementation using Chatterbot"""

    def __init__(self, config: MusharingChatbotConfig):
        super().__init__()

        self.chatbot = ChatBot(
            'muvtuber',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///db/muvtuber.sqlite3')
        self.chatbot.logger.setLevel(logging.ERROR)

    def ask(self, session_id: str, prompt: str, **kwargs) -> str:
        """Ask Chatbot with prompt, return response text

        Raises:
            ChatbotError: Chatbot error
        """
        return str(self.chatbot.get_response(prompt))


class MusharingChatbotFactory(chatbotapiv2.ChatbotFactory):
    def create_chatbot(self, config: MusharingChatbotConfig) -> MusharingChatbot:
        return MusharingChatbot(config)


if __name__ == "__main__":
    chatbot = MusharingChatbot(MusharingChatbotConfig())
    while True:
        print(chatbot.ask('', input("> ")))
