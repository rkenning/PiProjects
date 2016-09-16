#import ptvsd
#ptvsd.enable_attach(secret='123567')

import time
import sounds as sd
import RPi.GPIO as GPIO
from sounds import sounds

GPIO.setmode(GPIO.BCM)



GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def callBack(channel):
    print channel
    if channel == 17:
        sd.play_sound(0)
    if channel == 18:
        sd.play_sound(1)
    if channel == 27:
        sd.play_sound(2)
    if channel == 22:
        sd.play_sound(3)
    if channel == 23:
        sd.play_sound(4)



def main():
    GPIO.add_event_detect(17,   GPIO.RISING, callback=callBack,   bouncetime=500)
    GPIO.add_event_detect(18,   GPIO.RISING, callback=callBack,   bouncetime=500)
    GPIO.add_event_detect(27,   GPIO.RISING, callback=callBack,   bouncetime=500)
    GPIO.add_event_detect(22,   GPIO.RISING, callback=callBack,   bouncetime=500)
    GPIO.add_event_detect(23,   GPIO.RISING, callback=callBack,   bouncetime=500)



    print "Running"
    
    try:
        raw_input()
    except KeyboardInterrupt:
        GPIO.cleanup()

    GPIO.cleanup()

if __name__ == "__main__":
    main()
