# pulse width modulation

import machine
import time
from time import sleep

LED = machine.Pin(25)

# create the PWM object
pwmLED = machine.PWM(LED)

timeDelay = 0.001

# set frequency and duty cycle between 0 (all off) and 1023 (all on)
# 512 -> %0% duty cycle

pwmLED.freq(5000)

while True:

    for dc in range(0, 1023):
        pwmLED.duty(dc)
        pwmLED
        time.sleep(timeDelay)

    for dc in range(1023, 0, -1):
        pwmLED.duty(dc)
        time.sleep(timeDelay)
