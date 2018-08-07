''' demo of reading a button, interrupt-based!
Two modes:
1. callback including updates on LED and OLED - not good practices
2. callback, properly defined. Requires program checks status (while True).
2017-0917 PePo DOES NOT WORK properly
          Pin method off/on replaced (MP 1.9.2), tested on WeMOS-OLED ESP32
2017-0808 PePo initial setup
'''
import micropython
import machine, time
import ssd1306

__LED_PIN = const(15) #GPIO15
__BUTTON_PIN = const(12) #GPIO12

# LED: define led to be set on / off by button
led = machine.Pin(__LED_PIN, machine.Pin.OUT)
led.value(False)
# status of led: True=on, False=off
led_state = False

# BUTTON: define button
button = machine.Pin(__BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
button_state = button.value()
print('Init: button_state = ', button_state)

# create i2c for OLED display
#Huzzah:
#i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
# WeMOS-OLED:
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5), freq=100000)
print('i2c.scan: ', i2c.scan())   #[60]
# OLED screen dimensions
__WIDTH = const(128)
__HEIGHT = const(64) #const(32)
oled = ssd1306.SSD1306_I2C(__WIDTH, __HEIGHT, i2c)

''' define callback with LED and OLED updates
# direct control of LED and OLED is not best practices. Why?
# => too slow and it hold up other processing
def callback_oled(p):
    print('button {0} pressed'.format(p))
    led.value(not led.value())
    refreshOLED(['LED: {0} '.format(led.value()),]) #LED value
#'''

#''' define a proper callback
def callback(p):
    global button_state#, led_state
    # best practices: set variabel and pick it up in other part of program
    #led_state = led.value()#not led_state
    button_state = button.value()#not button_state #p.value()
#'''

# helper to refresh OLED display
def refreshOLED(msg):
    oled.fill(0) # clear oled
    oled.text('Button demo',0,0) #header
    oled.text(msg[0],0,10)
    if len(msg) > 1:
        oled.text(msg[1],0,20)
    oled.show()

#define buton-click interrupt on falling edge due to PULL_UP!
''' using a 'slow' callback
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback_oled)
refreshOLED('Press button!')
oled.show()
print('done')
#'''

#''' using proper callback
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)
#print('done')

# required to have a loop to display current status of led...
def run():
    while True:
        if not led_state and button_state:
            led.value(True)
            led_state = True
        elif led_state and not button_state:
            led.value(False)
            led_state = False
        refreshOLED(['LED: {0} '.format(led_state), 'BTN: {0} '.format(button_state)])

# the demo
try:
    print('Button demo')
    refreshOLED(['Press button!',])
    run()
except:
    print('Done')
    refreshOLED(['Done!',])
#'''
