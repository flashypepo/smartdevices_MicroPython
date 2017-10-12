# button.py: demo of reading a button state.
# 2017_0917 PePo new and added debounce
# based upon https://learn.adafruit.com/micropython-hardware-digital-i-slash-o/digital-inputs?view=all
import machine, time

# setup button
BUTTON_PIN = 13 #Huzzah, interne pull-up
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
# button.value() -> 0: button pressed
# button.value() -> 1: button released

''' naive reading button
def run():
    while True:
        if not button.value():
            print('Button pressed!')
#'''

# demo2: take care of debounce
# The way it works is the code looks for
# only when the input pin changes from a
# high to low level (the button was just pressed)
# or a low to high level (the button was just released).
# By looking for this change instead of a constant
# pressed or not pressed value the code can print
# a message once instead of repeatedly
'''
table for variables first, second, and its effect and display/LED state
first second  Effect                                         Display/LED
0      0      button is pressed continously                    off
0      1      button is changed from pressed to not-pressed    on  -> off
1      0      button is changed from not-pressed to pressed    off -> on
1      1      button is not pressed continously                off
'''

''' demo2
def run():
    while True:
        first = button.value()
        time.sleep(0.01)
        second = button.value()
        # check for changes!
        if first and not second:
            print('Button pressed!')
        elif not first and second:
            print('Button released!')
#'''

#''' demo3:
# press button: LED is on
# release button: LED off
# Break/Ctrl-C: user-friendly termination of demo3

led = machine.Pin(15, machine.Pin.OUT) # GPIO15
led.value(0) # LED is off by-default

def run():
    try:
        while True:
            first = button.value() # get first value
            time.sleep(0.01)
            second = button.value() #get 2nd value
            # check for changes!
            # Note: if nothing was changed: do nothing!
            if first and not second:
                led.value(1)
                print('Knop ingedrukt!')
            elif not first and second:
                led.value(0)
                print('Knop losgelaten!')
    except:
        print('Demo done')
        led.value(0)
#'''

# execute one of the demo's by uncommenting
run()
