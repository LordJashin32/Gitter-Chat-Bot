#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
from gitterpy.client import GitterClient
import json

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

chatbot = ChatBot(
    "treehouses-bot", # Name of your bot
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
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

gitter_api_token='YOUR-API-TOKEN' # Gitter API token
gitter_room='YOUR-ROOM/YOUR-SUB-ROOM' # Gitter Room Name

gitter = GitterClient(gitter_api_token)
while True:
    try:
        response = gitter.stream.chat_messages(gitter_room)
        for stream_messages in response.iter_lines():
            if is_json(stream_messages):
                resp = json.loads(stream_messages)
                if 'msg' in globals():
                    if resp['text'] == msg:
                        continue
                if 'botresp' in globals():
                    if str(botresp) == msg:
                        continue
                msg = resp['text']
                userid = resp['fromUser']['username']
                if userid == gitter.auth.get_my_id['name']:
                    continue
                botresp = chatbot.get_response(msg)
                if botresp != "":
                    if "The current time" not in str(botresp):
                      gitter.messages.send(gitter_room, "@" + userid + " " + str(botresp))
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
