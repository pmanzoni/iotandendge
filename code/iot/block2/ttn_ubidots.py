import sys
import time
import base64

import json
import struct

import paho.mqtt.client as mqtt

def on_connectTTN(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe(...)

def on_connectUBI(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

# The callback for when a message is received from the server.
def on_messageTTN(client, userdata, msg):
#    print("sisub: msg received with topic: {} and payload: {}".format(msg.topic, str(msg.payload)))
    print("sisub: msg received with topic: {} ".format(msg.topic))

    if (msg.topic == "v3/lopys2ttn@ttn/devices/lopy4sense/up"):

        themsg = json.loads(msg.payload.decode("utf-8"))
        dpayload = themsg["uplink_message"]["decoded_payload"]
#        print(dpayload)

        print("@%s >> temp=%.3f hum=%.3f lux=%.3f" % (time.strftime("%H:%M:%S"), dpayload["temperature"], dpayload["lux"], dpayload["humidity"]))



        clientUBI.publish(...)



clientTTN = mqtt.Client()
clientUBI = mqtt.Client()

clientTTN.on_connect = on_connectTTN
clientTTN.on_message = on_messageTTN
clientUBI.on_connect = on_connectUBI

clientTTN.username_pw_set(...)
clientTTN.connect(...)

clientUBI.username_pw_set(...)
clientUBI.connect(...)

clientTTN.loop_forever()

