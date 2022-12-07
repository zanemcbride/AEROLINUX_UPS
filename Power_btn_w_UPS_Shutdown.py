import smbus
import time
import os
import RPi.GPIO as GPIO

#set pin 6 as btn and call shutdown if pressed
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(6, GPIO.FALLING, callback=Shutdown, bouncetime=2000)



addr=0x10 #ups i2c address
bus=smbus.SMBus(1) #i2c-1
vcellH=bus.read_byte_data(addr,0x03)
vcellL=bus.read_byte_data(addr,0x04)
socH=bus.read_byte_data(addr,0x05)
socL=bus.read_byte_data(addr,0x06)

f= open("UPS_SHUTDOWN_THRESHOLD.txt", "r")
threshold=int((f.readline()))

#capacity=(((vcellH&0x0F)<<8)+vcellL)*1.25 #capacity
#electricity=((socH<<8)+socL)*0.003906 #current electric quantity percentage

def Shutdown(channel):
	print("SHUTTING DOWN")
	time.sleep(5)
	os.system("sudo shutdown -h now")
	
def Shutdown():
	print("SHUTTING DOWN")
	time.sleep(5)
	os.system("sudo shutdown -h now")

GPIO.add_event_detect(6, GPIO.FALLING, callback=Shutdown, bouncetime=2000)

while 1:
    socH=bus.read_byte_data(addr,0x05)
    socL=bus.read_byte_data(addr,0x06)
    #capacity=(((vcellH&0x0F)<<8)+vcellL)*1.25 #capacity
    electricity=((socH<<8)+socL)*0.003906 #current electric quantity percentage
    
    #print("capacity=%dmV"%capacity)
    print("battery percentage=%.2f"%electricity)
    
    if electricity<threshold:
        Shutdown()
        
    time.sleep(5)

print("capacity=%dmV"%capacity)
print("electricity percentage=%.2f"%electricity)
