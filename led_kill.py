# Ben Woodfield
# Pin De-Activate - quick script

import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(23, RPi.GPIO.OUT)
RPi.GPIO.setup(4, RPi.GPIO.OUT)

RPi.GPIO.output(23, False)
print 'GPIO pin is now OFF'
RPi.GPIO.output(4, False)
