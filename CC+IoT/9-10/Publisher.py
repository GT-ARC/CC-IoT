#!/usr/bin/env python
import time

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
   print("Connected with result code"+ str(rc))

#client =  mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv31
)
client = mqtt.Client("zzzzzzzz", protocol=mqtt.MQTTv31)
client.on_connect = on_connect

client.connect("fe80::f87c:f7ed:c0f7:1395%lowpan0",1883,60)
client.loop_start()

while True:
    time.sleep(3)
    client.publish("test/temperature","test")
