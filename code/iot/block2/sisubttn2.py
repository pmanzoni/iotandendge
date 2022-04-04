import paho.mqtt.client as mqtt
import json

THE_BROKER = "eu1.cloud.thethings.network"
THE_TOPIC = "v3/+/devices/#"
CLIENT_ID = ""

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe(THE_TOPIC, qos=0)

def on_message(client, userdata, msg):

	themsg = json.loads(msg.payload.decode("utf-8"))
	dpayload = themsg["uplink_message"]["decoded_payload"]

	print("%s >> temp=%.3f hum=%.3f lux=%.3f" % ("Got these values ", dpayload["temperature"], dpayload["lux"], dpayload["humidity"]))

client = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("lopys2ttn@ttn", password="NNSXS.A55Z2P4YCHH2RQ7ONQVXFCX2IPMPJQLXAPKQSWQ.A5AB4GALMW623GZMJEWNIVRQSMRMZF4CHDBTTEQYRAOFKBH35G2A")
client.connect(THE_BROKER, port=1883, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()

