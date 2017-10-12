# OLED demo, gebasseerd op tutorials van Tony DiCola/Adafruit
# Arduino-stijl: 'setup' en 'loop'
# Pre-conditions
#     * micropython v1.9 en hoger, het moet module importeren ondersteunen
#     * ssd1306.mpy op de ESP8266 aanwezig, zie [1]
#       download from: https://github.com/adafruit/micropython-adafruit-ssd1306/releases
# History:
#     2017_1001 PePo nieuw uit Adafruit's tutorials [1], [2] en [3]
# Sources:
# [1] https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display?view=all#micropython
# [2]
# [3]
# Author: Tony DiCola
# License: Public Domain

########################################################################
# Setup code goes below, this is called once at the start of the program: #
########################################################################
import machine, time
import ssd1306   #module voor de OLED-chip SSD1306

# 2017_0422 PePo: dimension in pixels of OLED display
_DISPLAY_WIDTH  = const(128)
_DISPLAY_HEIGHT = const(64)   # LoLin-ESP32-OLED
#_DISPLAY_HEIGHT = const(32)  # Smart Devices

# setup I2C protocol, using hardware I2C-pins
''' SCL/SDA port on Huzzah ESP8266 (Smart Devices) - zie pinlayout
SCL = 5 #pin: IO5 / SCL - Clock signal
SDA = 4 #pin: IO4 / SDA - Data signal
#'''
#''' SCL/SDA port on LoLin-ESP32-OLED - zie pinlayout
SCL = 4  # Clock signal
SDA = 5  # Data signal
#'''
i2c = machine.I2C(scl=machine.Pin(SCL), sda=machine.Pin(SDA))
#i2c.scan()   #check address of OLED-display: [60]

# create OLED object
oled = ssd1306.SSD1306_I2C(_DISPLAY_WIDTH, _DISPLAY_HEIGHT, i2c)
'''handmatige erase - niet echt nodig op dit punt
oled.fill(0) # fill buffer with 0 i.e. blank the oled
#DO:oled.fill(1) # fill buffer with 1 i.e. oled is white rectangle
oled.show() # display the buffer
#'''

# function erase(), erased the OLED-display i.e. blank it
def erase():
    oled.fill(0)
    oled.show()

# blinky: display toggles between on (white/blue) and off (black)
def blink():
    erase() #black display
    time.sleep(1)
    oled.fill(1) #white/blue display
    oled.show()
    time.sleep(1)

# pixel drawing: display pixels in corners
def corners(value = 1):
    oled.pixel(128, 0, value)
    oled.pixel(127, 0, value)
    oled.pixel(0, 63, value)
    oled.pixel(127, 63, value)
    oled.show()

def message (x, y, msg):
    oled.fill(0)
    l = len(msg) # number of messages
    for i in range(l):
        oled.text(msg[i], x, y + 10 * i)
    oled.show()

###################################################################
# Loop code goes inside the loop here, this is called repeatedly: #
###################################################################
while True:
    #blink()
    #corners(1) #ON
    #time.sleep(1)
    #corners(0) #OFF
    message(0, 0, ['Hello','World'])
