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
# Huzzah: pin#2 blue led, pin#0 red led
#LED_PIN = 0 # red LED
LED_PIN = 2 # blue LED
led = machine.Pin(LED_PIN, machine.Pin.OUT) #builtin LED Feather Huzzah

led.value(1) # init led OFF
time.sleep(0.1) # wait

while True:
    ###################################################################
    # Loop code goes inside the loop here, this is called repeatedly: #
    ###################################################################
    led.value(0) # on
    time.sleep(0.5)
    led.value(1) # off
    time.sleep(0.5)
