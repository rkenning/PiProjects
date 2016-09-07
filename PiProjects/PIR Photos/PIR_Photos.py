#!/usr/bin/env python
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import time
import os
import gdrive
import itertools

current_milli_time = lambda: int(round(time.time() * 1000))

LedPin = 11    # pin11 --- led
BtnPin = 12    # pin12 --- button
PIRPin = 8	   # pink 7 - PIR

camera = PiCamera()
camera.resolution = (1024, 786)
camera.rotation = 180
photo_path = '/home/pi/GDrive/Pics/'


def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	#GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	#GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.setup(PIRPin, GPIO.IN)
	#GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def takePhoto():
    print "Taking pictures" 
    camera.start_preview() # Capture Picture
    #Loop 5 times
    for i in range(0, 5):
        filename = 'image'+str(current_milli_time())+'.jpg'
        print "Taking Picture :" + filename
        camera.capture(photo_path+filename)
        gdrive.upload(photo_path+filename)
        sleep(5)
        camera.stop_preview()


def my_callback(channel):  
    if GPIO.input(PIRPin):     # if port 25 == 1  
        takePhoto()        
        sleep(1)
    else:                  # if port 25 != 1  
        print "Falling edge detected on 25"  


def loop():
    while True:
        if GPIO.input(PIRPin) == GPIO.LOW: # Check whether the button is pressed or not.
            print '...LOW'
        else:
            print 'HIGH...'
        
        sleep(1)
       
def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    takePhoto()
    setup()
    GPIO.add_event_detect(PIRPin, GPIO.BOTH, callback=my_callback)
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        camera.stop_preview()
		#GPIO.output(LedPin, GPIO.HIGH)     # led off
		#GPIO.cleanup(LedPin)   # Set LedPin's mode is output
		#GPIO.cleanup(BtnPin)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
        GPIO.cleanup(PIRPin)
        destroy()
destroy()   

