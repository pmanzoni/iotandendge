import argparse
import base64
import json
import logging
import signal
import struct
import sys
import time

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import paho.mqtt.client as mqtt
from datetime import datetime, timezone

r_value = "VOID"


def on_connect(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe("v3/+/devices/#", qos=0)


def on_message(client, userdata, msg):
    global r_value
    print("msg received with topic: {} and payload: {}".format(
        msg.topic, str(msg.payload)))

    if (msg.topic == "v3/lopys2ttn@ttn/devices/lopy4sense/up"):

        themsg = json.loads(msg.payload.decode("utf-8"))
        dpayload = themsg["uplink_message"]["decoded_payload"]

        print("@%s >> temp=%.3f hum=%.3f lux=%.3f" %
              (time.strftime("%H:%M:%S"), dpayload["temperature"],
               dpayload["lux"], dpayload["humidity"]))

        r_value = dpayload["temperature"]


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")


def getdata(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=str(r_value))


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Sorry, I didn't understand that command.")


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(
    "___FILL_IN_HERE___@ttn",
    password=
    "___FILL_IN_HERE___"
)
client.connect("___FILL_IN_HERE___", port=1883, keepalive=60)
client.loop_start()


updater = Updater(token='___FILL_IN_HERE___', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

getdata_handler = CommandHandler('getdata', getdata, pass_args=False)
dispatcher.add_handler(getdata_handler)

unknown_handler = MessageHandler(Filters.text & (~Filters.command), unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()

updater.idle()
