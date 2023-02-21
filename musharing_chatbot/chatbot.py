# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create a new chat bot
_chatbot = ChatBot('muvtuber',
                   storage_adapter='chatterbot.storage.SQLStorageAdapter',
                   database_uri='sqlite:///db/muvtuber.sqlite3')


def chat(prompt: str) -> str:
    """chat with the bot
    :param prompt: your input
    :return: the bot's response as a string
    """
    return str(_chatbot.get_response(prompt))


def train_default(chatbot: ChatBot) -> None:
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    trainer.train("chatterbot.copus.chinese")


if __name__ == "__main__":
    # train_default(_chatbot)
    print(chat("你好"))
    while True:
        print(chat(input("> ")))
