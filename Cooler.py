import RPi.GPIO as GPIO
# import sys, traceback
from time import sleep

from settings import settings
from Logger import Logger
from utils import get_temp

class Cooler:
    """
    Init the pins and launch temp check
    """
    def __init__(self):
        self.pin_state = False   # the pin's state
        self.cfg_parse()    # parse the configs

        self.logger = Logger(logs_dir=self.log_dir)  # init the logger

        # Initalize the pins
        GPIO.setmode(GPIO.BCM)  # the numeric mode
        GPIO.setup(self.control_pin, GPIO.OUT, inital=0) # set the OUTPUT mode to signal pin

        try:
            self.main()
        except Exception as e:
            self.logger.error_traceback(e)
        finally:
            GPIO.cleanup()
            self.logger.close()

    def cfg_parse(self):
        self.temp_on = settings['temp_on']
        self.temp_off = settings['temp_off']
        self.control_pin = settings['control_pin']
        self.sleep_time = settings['sleep_time']
        self.log_freq = settings['log_freq']
        self.log_dir = settings['log_dir']

        if self.temp_off >= self.temp_on:   # check the logical relation
            raise ValueError("temp_on must be greater than temp_off")

    def main(self):
        iterator = 0
        while True:
            temp = get_temp()   # get the temperature

            if temp >= self.temp_on and not self.pin_state or temp < self.temp_off and self.pin_state:
                self.pin_state = not self.pin_state   # change the state
                GPIO.output(self.control_pin, self.pin_state) # set the new state to pin

                iterator += 1
                sleep(self.sleep_time)

                if iterator >= self.log_freq:   # log the temp if need iteration was achieved
                    self.logger.info(temp)
                    iterator = 0
