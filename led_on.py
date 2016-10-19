# Ben Woodfield
# GPIO Pin Activation - quick script
# Turns pins/LED/Hardware ON constantly

import RPi.GPIO
import time

# Here I activate GPIO 23 and GPIO 4
# Change this if needed to your desired Pins / See my RPi Pinout chart - or your specific RPi model GPIO chart
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(23, RPi.GPIO.OUT)
RPi.GPIO.setup(4, RPi.GPIO.OUT)

RPi.GPIO.output(23, True)
RPi.GPIO.output(4, True)
print 'GPIO pin is activated continuously'
