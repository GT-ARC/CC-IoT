#!/usr/bin/env python

# Class for DHT22 temperature and humidity sensor

from Abstract import SensorAbstract

# sudo apt-get install python-pip
# pip freeze | grep RPi
import RPi.GPIO as GPIO
import time

class SensorHCSR04(SensorAbstract):

    def __init__(self):
        super(SensorHCSR04, self).__init__()

    # Sensor initializion
    def setup(self):
        # use Raspberry Pi board pin numbers
        GPIO.setmode(GPIO.BOARD)

        # set GPIO Pins
        global PIN_TRIGGER, PIN_ECHO
        PIN_TRIGGER = 7
        PIN_ECHO = 11

        print ("Distance Measurment In Progress")

        # set GPIO input and output channels
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

    def measure(self):
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

        return distance

if __name__ == '__main__':
    mySensorHCSR04 = SensorHCSR04()
    mySensorHCSR04.setup()
    while True:
        mySensorHCSR04.measure()
        time.sleep(1)
    
    
    
