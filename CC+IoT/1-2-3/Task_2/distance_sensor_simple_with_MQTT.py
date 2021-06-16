import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

HOST = "test.mosquitto.org"
PORT = 1883

client = mqtt.Client()
client.connect(HOST, PORT)


# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set GPIO Pins
PIN_TRIGGER = 7
PIN_ECHO = 11

print("Distance Measurment In Progress")

# set GPIO input and output channels
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

while True:
        # set Trigger to HIGH
        GPIO.output(PIN_TRIGGER, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, False)

        startTime = time.time()
        stopTime = time.time()

        # save start time
        while GPIO.input(PIN_ECHO) == 0:
                pass
        startTime = time.time()

        # save time of arrival
        while GPIO.input(PIN_ECHO) == 1:
                pass
        stopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = stopTime - startTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        print ("Distance: %.1f cm" % distance)

        client.publish("/test/distance", "Distance={0:0.1f} cm".format(distance))
        client.subscribe("/test/distance")

        time.sleep(1)