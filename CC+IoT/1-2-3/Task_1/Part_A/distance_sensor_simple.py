import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

PIN_TRIGGER = 7
PIN_ECHO = 11

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

while True:
        GPIO.output(PIN_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, False)

        startTime = time.time()
        stopTime = time.time()

        while GPIO.input(PIN_ECHO) == 0:
                pass
        startTime = time.time()

        while GPIO.input(PIN_ECHO) == 1:
                pass
        stopTime = time.time()


        # time difference between start and arrival
        TimeElapsed = stopTime - startTime

        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        print ("Distance: %.1f cm" % distance)

        time.sleep(1)
