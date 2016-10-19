# Ben Woodfield
# Pin De-Activation - quick script
# Use this to turn OFF GPIO pins

import RPi.GPIO
import time

# Change the Pin numbers accordingly for your requirements
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(23, RPi.GPIO.OUT)
RPi.GPIO.setup(4, RPi.GPIO.OUT)

RPi.GPIO.output(23, False)
print 'GPIO pin is now OFF'
RPi.GPIO.output(4, False)
