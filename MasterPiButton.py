import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

PrevButtonPin = 15  
ResetButtonPin = 13
NextButtonPin = 11

GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location

GPIO.setup(PrevButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Set PrevButtonPin as input and enable pullup resistor
GPIO.setup(ResetButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Set ResetButtonPin as input and enable pullup resistor
GPIO.setup(NextButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Set NextButtonPin as input and enable pullup resistor


def nextPressed(channel):
    print('Next Pressed')
    
def prevPressed(channel):
    print('Prev Pressed') #Display button pressed
    
def resetPressed(channel):
    print('Reset Pressed')
    
GPIO.add_event_detect(PrevButtonPin,GPIO.FALLING,callback=prevPressed,bouncetime=200)
GPIO.add_event_detect(ResetButtonPin,GPIO.FALLING,callback=resetPressed,bouncetime=200)
GPIO.add_event_detect(NextButtonPin,GPIO.FALLING,callback=nextPressed,bouncetime=200)

message=input("Press any key then press enter to exit program\n")

GPIO.cleanup(); #Clean up when exiting the program