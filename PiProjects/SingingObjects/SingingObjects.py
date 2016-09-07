import ptvsd
ptvsd.enable_attach(secret='123567')

import time
import pygame.mixer
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pygame.mixer.init(48000, -16, 1, 1024)
soundChannelList = [None] * 12
soundList = [None] * 12

sound1 = pygame.mixer.Sound("Spoon.wav")
soundChannel1 = pygame.mixer.Channel(1)
soundList[0] = sound1
soundChannelList[0] = soundChannel1

sound2 = pygame.mixer.Sound("Banana.wav")
soundChannel2 = pygame.mixer.Channel(2)
soundList[2] = sound2
soundChannelList[1] = soundChannel2

sound3 = pygame.mixer.Sound("Fork.wav")
soundChannel3 = pygame.mixer.Channel(3)
soundList[3] = sound3
soundChannelList[3] = soundChannel3

padPin = 17
GPIO.setup(padPin, GPIO.IN)


alreadyPressed = False

while True:
    print "started"

    padPressed =  GPIO.input(padPin)

    if padPressed and not alreadyPressed:
        print "pressed"
        soundChannel = soundChannelList[0]
        sound = soundList[0]
        soundChannel.play(sound)

    alreadyPressed = padPressed
    time.sleep(0.1)

