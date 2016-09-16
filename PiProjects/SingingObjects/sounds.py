import pygame.mixer
import sounds

pygame.mixer.init(48000, -16, 1, 1024)
soundChannelList = [None] * 12
soundList = [None] * 12


sound0 = pygame.mixer.Sound("Spoon.wav")
soundChannel0 = pygame.mixer.Channel(0)
soundList[0] = sound0
soundChannelList[0] = soundChannel0

sound1 = pygame.mixer.Sound("Banana.wav")
soundChannel1 = pygame.mixer.Channel(1)
soundList[1] = sound1
soundChannelList[1] = soundChannel1

sound2 = pygame.mixer.Sound("Fork.wav")
soundChannel2 = pygame.mixer.Channel(2)
soundList[2] = sound2
soundChannelList[2] = soundChannel2

sound3 = pygame.mixer.Sound("Pear.wav")
soundChannel3 = pygame.mixer.Channel(3)
soundList[3] = sound3
soundChannelList[3] = soundChannel3

sound4 = pygame.mixer.Sound("Orange.wav")
soundChannel4 = pygame.mixer.Channel(4)
soundList[4] = sound4
soundChannelList[4] = soundChannel4

def play_sound(Sound_Number):
    soundChannel = soundChannelList[Sound_Number]
    sound = soundList[Sound_Number]
    soundChannel.play(sound)
