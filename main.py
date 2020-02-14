#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import UbuntuCorpusTrainer
from gitterpy.client import GitterClient
import json

chatbot = ChatBot(
    "YOUR_BOT_NAME", # Name of your bot
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'    ]
)

# Run this once to generate good stuff for database to start with
# Warning takes 6 hours approximately to run
#trainer = UbuntuCorpusTrainer(chatbot)
#trainer.train()

gitter_api_token='YOUR_API_KEY' # Gitter API token
gitter_room='YOUR_ROOM/YOUR_SUB_ROOM' # Gitter Room Name

gitter = GitterClient(gitter_api_token)
while True:
    try:
        response = gitter.stream.chat_messages(gitter_room)
        for stream_messages in response.iter_lines():
            if stream_messages != "":
                resp = json.loads(stream_messages)
                msg = resp['text']
                userid = resp['fromUser']['username']
                if userid == gitter.auth.get_my_id['name']:
                    continue
                gitter.messages.send(gitter_room, "@" + userid + " " + chatbot.get_response(msg))
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
