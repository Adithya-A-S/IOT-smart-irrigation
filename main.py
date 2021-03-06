import time
import paho.mqtt.client as paho
from paho import mqtt
from weather_score import ws
from keep_alive import keep_alive

keep_alive()


def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)


def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("weather_score", "Score123")
client.connect("4434863454a64154b81bab7294207c19.s1.eu.hivemq.cloud", 8883)
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish
#client.publish("weather_score/ws", payload=str(x), qos=1)

while True:
    x = ws()
    client.connect("4434863454a64154b81bab7294207c19.s1.eu.hivemq.cloud", 8883)
    client.publish("weather_score/ws", payload=str(x), qos=1)
    time.sleep(1)
client.loop_forever()
