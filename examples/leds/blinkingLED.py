# Example of a blinking led in micropython
# Arduino style: setup and loop
#
# 2016-1022 PePo builtin LED is GPIO 2, which has pull-up to Vcc
# micropython v1.9.* DEPRECATED: led.high() and led.low()
#
# 2016-0903 PePo, based upon
#  https://learn.adafruit.com/micropython-basics-blink-a-led/blink-led

###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import machine
import time
print('Blinking LED...')

# -------- configuration LED pin ------------------
# Huzzah built-in LED pin=2 blue led, pin=0 red led
# extern LED: pin=15 red led
#LED_PIN = 0 # red LED
#LED_PIN = 2 # blue LED
LED_PIN = 15 # exter red LED

# create led-object
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# sleep delay
# DELAY = 2 #0.5

while True:
    ###################################################################
    # Loop code goes inside the loop here, this is called repeatedly: #
    ###################################################################
    #'''
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)
    #'''

    ''' alternatiev loop
    while True:
        led.value( not led.value() )
        time.sleep(DELAY)
    #'''
