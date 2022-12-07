#!/bin/python

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Shutdown(channel):
	print("SHUTTING DOWN")
	time.sleep(5)
	os.system("sudo shutdown -h now")

GPIO.add_event_detect(6, GPIO.FALLING, callback=self.Shutdown, bouncetime=2000)

while 1:
	time.sleep(1)
