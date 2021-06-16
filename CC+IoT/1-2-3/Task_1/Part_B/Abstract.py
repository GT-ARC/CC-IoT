#!/usr/bin/env python

# An abstract parent class for all sensors

from abc import ABCMeta, abstractmethod
import time

class SensorAbstract:
    __metaclass__ = ABCMeta

    def __init__(self):
        # Setup sensor
        self.setup() 

    # Sensor initialization
    @abstractmethod
    def setup(self):
        pass

    # Sensor measurement function
    @abstractmethod
    def measure(self):
        pass
