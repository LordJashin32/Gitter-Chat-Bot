#!/usr/bin/python3
# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.conversation import Statement

chatbot = ChatBot(
    "My ChatterBot", # Name of your bot
    input_adapter="chatterbot.input.Gitter",
    output_adapter="chatterbot.output.Gitter",
    gitter_api_token="my-gitter-api-token", # Gitter API token
    gitter_room="my-room-name", # Gitter Room Name
    gitter_only_respond_to_mentions=False, # Bot responds to all messages in room
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'    ]
)

# 500mb but gives us very good responses to start with
trainer = UbuntuCorpusTrainer(chatbot)

# Enter your own custom stuff here
trainer1 = ListTrainer(chatbot)
trainer1.train([
    "Input question user asks on gitter?",
    "Response that the bot will give to question on gitter above.",
])

# Start by training our bot with the Ubuntu corpus data
trainer.train()

while True:
    try:
        response = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
