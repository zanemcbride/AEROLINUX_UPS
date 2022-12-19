# this script creates a power button  on pin 26 and shuts down the
#pi if the UPS battery gets to low

import smbus
import time
import os
import RPi.GPIO as GPIO


#set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) #power btn
GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH) #for power indication LED


#start comm and read power levels from UPS HAT
addr=0x10 #ups i2c address
bus=smbus.SMBus(1) #i2c-1
vcellH=bus.read_byte_data(addr,0x03)
vcellL=bus.read_byte_data(addr,0x04)
socH=bus.read_byte_data(addr,0x05)
socL=bus.read_byte_data(addr,0x06)

#txt file for setting UPS battery cut off threshold
f= open("/home/pi/AEROLINUX_UPS/UPS_SHUTDOWN_THRESHOLD.txt", "r")
threshold=int((f.readline()))



def btn_Shutdown(channel):
	print("SHUTTING DOWN")
	time.sleep(5)
	os.system("sudo shutdown -h now")


def Shutdown():
	print("SHUTTING DOWN")
	time.sleep(5)
	os.system("sudo shutdown -h now")

#power btn
GPIO.add_event_detect(6, GPIO.FALLING, callback=btn_Shutdown, bouncetime=2000)

while 1:
#read battery level
    socH=bus.read_byte_data(addr,0x05)
    socL=bus.read_byte_data(addr,0x06)
    electricity=((socH<<8)+socL)*0.003906 #current electric quantity percentage
    
    #print battery percentage
    print("battery percentage=%.2f"%electricity)
    
    if electricity<threshold:
        Shutdown()
        
    time.sleep(5)


