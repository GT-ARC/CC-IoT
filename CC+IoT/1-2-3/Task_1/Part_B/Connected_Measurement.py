#!/usr/bin/env python

from Abstract import SensorAbstract
from Sensor import SensorHCSR04
import paho.mqtt.client as mqtt
import time

class ConnectionSensor:
    def __init__(self, sensor, HOST, PORT, topic):
        self.client = mqtt.Client()
        self.sensor = sensor
        self.HOST = HOST
        self.PORT = PORT
        self.topic = topic

    def connect(self):
        print("Connecting to MQTT brocker ...")
        self.client.connect(self.HOST, self.PORT)
        print("Connecting successful!")

    def measurement(self):
        distance = self.sensor.measure()

        # Subscribe to topic
        self.topic = "/test/distance"
        self.client.publish(self.topic, "Distance={0:0.1f} cm".format(distance))
        #self.client.subscribe(self.topic)


if __name__ == '__main__':
    mySensorHCSR04 = SensorHCSR04()
    mySensorHCSR04.setup()
    connection = ConnectionSensor(mySensorHCSR04, "test.mosquitto.org", 1883, "/test/distance")
    connection.connect()
    while True:
        connection.measurement()
        time.sleep(1)
