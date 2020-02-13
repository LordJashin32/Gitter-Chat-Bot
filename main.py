#!/usr/bin/python3

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    "My ChatterBot",
    output_adapter="chatterbot.output.Gitter",
    gitter_api_token="my-gitter-api-token",
    gitter_room="my-room-name",
    gitter_only_respond_to_mentions=False,
)
print('Hello World')


trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)