# Run the following command to install the DHT library to your Raspberry Pi.
#
# sudo pip3 install Adafruit_DHT
#
import Adafruit_DHT
import time
import paho.mqtt.client as mqtt

HOST = "test.mosquitto.org"
PORT = 1883
topic = "/test/temperature"

client = mqtt.Client()

client.connect(HOST, PORT)

# use the library to talk and interact with the DHT22 sensor.
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temperature={0:0.1f}*C   Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")

    client.publish(topic, "Temperature={0:0.1f}*C   Humidity={1:0.1f}%".format(temperature, humidity))

    time.sleep(2)