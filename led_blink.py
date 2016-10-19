# Ben Woodfield
# A program to interact with RPi GPIO Pins
# Import the GPIO commands - and set the desired GPIO Pin Number

import RPi.GPIO
import time

# Here I am activating 2 pins for OUTPUT use.
# GPIO 0 and GPIO 1
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(0, RPi.GPIO.OUT)
RPi.GPIO.setup(1, RPi.GPIO.OUT)

# Change time.sleep() to your preferred blink rate
while True:
    RPi.GPIO.output(0, True)
    RPi.GPIO.output(1, False)
    time.sleep(0.25)
    print "Tick"
       
    RPi.GPIO.output(0, False)
    RPi.GPIO.output(1, True)
    time.sleep(0.25)
    print "Tock"

#while RPi.GPIO.output(23, True):
#    RPi.GPIO.output(4, False)

#while RPi.GPIO.output(23, False):
#    RPi.GPIO.output(4, True)

    
# To Disable the Pin - Run this alone - With correct Pin No
#RPi.GPIO.output(23, False)




    
