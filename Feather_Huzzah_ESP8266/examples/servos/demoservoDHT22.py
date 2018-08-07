# demo sevro motor, showing PWM and humidity mapping
# servo is connected to GPIO15
# DHT22 is connected to GPIO12
# 2017-1008 PePo demo for college #6

import machine, time
import ssd1306
# module servo.py on Smartworld >> SmartDevices
# It's a modified servo module from DiCola: extended with deinit()
import servo  #use servo module DiCola, extended with deinit()

# create servo object - default arguments
s = servo.Servo(machine.Pin(15))

''' test: sweep servo from angle 0 to 180 and back
# MOB-section
def test(s):
    # sweep from angle 0 to 180
    print('go...')
    for i in range(0, 180):
        print('angle: ', i)
        s.write_angle(i)
        time.sleep(0.2)

    time.sleep(1)

    print('and back...')
    for i in range(180, 0, -1):
        print('angle: ', i)
        s.write_angle(i)
        time.sleep(0.2)
test(s)
#'''

# move servo forwards: increase angle
def forward(s, p1 = 0, p2=180, dt=0.1):
    for i in range(p1, p2):
        print('angle:', i)
        s.write_angle(i)
        time.sleep(dt)

# move servo backwards: decrease angle
def backward(s, p1 = 180, p2=0, dt=0.1):
    for i in range(p1, p2, -1):
        print('angle:', i)
        s.write_angle(i)
        time.sleep(dt)

''' demo1: move servo s from 0 to 180 and back
def demo1(s):
    forward(s)
    time.sleep(1)
    backward(s)
demo1(s)
#'''


# use oled for displaying data
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
print(i2c.scan())
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
#oled.fill(1)
#oled.show()
#time.sleep(2)

#''' function to show a message on OLED
def disp_msg(msg, x=0, y=0):
    #oled.fill(0)
    oled.text(msg, x, y)
    oled.show()
#disp_msg('hello world', 0,0)


''' demo2: move servo from 0 to 180 and show angle on OLED
def demo2(s, p1=0, p2=180, dt=0.1):
    # move servo with increasing angle (forward)
    for i in range(p1, p2):
        disp_msg('angle: {0}'.format(i))
        s.write_angle(i)
        time.sleep(dt)
    time.sleep(1)
    # move servo with decreasing angle (back)
    for i in range(p2, p1, -1):
        disp_msg('angle: {0}'.format(i))
        s.write_angle(i)
        time.sleep(dt)
demo2(s)
#'''

#''' demo3: map humidity to servo position
# humidity: 50 - 100
# servo: 0 - 180
# servo_positie = humidity - 50
# Linear interpolation helper:
#     maps x in range inMin..inMax into outMin..outMax
def _map(x, inMin, inMax, outMin, outMax):
    return outMin + (x - inMin) * ((outMax - outMin) / (inMax - inMin))

import dht
# create DHT22 sensor object
sensor = dht.DHT22(machine.Pin(12))

#''' demo3 - set angle servo on vlaue humidity
def demo3(s, dt=2.5):
    # get sensor data
    sensor.measure()
    #t = sensor.temperature()
    humidity = sensor.humidity()

    # display sensor data on OLED
    oled.text('Sensor DHT22',0, 0)
    oled.text('Humidity {0:0.1f} %'.format(humidity),0, 10)
    oled.show()

    # map value humidity into angle for servo position
    angle = int(_map(humidity, 40, 110, 0, 180))
    disp_msg('angle: {0}'.format(angle), 0, 20)
    s.write_angle(angle)

    # wait between measurements
    # time delay must be at least 2 seconds for sensor
    time.sleep(dt)

def erase():
    oled.fill(0)
    oled.show()

try:
    while True:
        erase()
        demo3(s)
except:
    s.deinit() #de-couple PWM fron GPIO
    erase() # blank OLED
    disp_msg('demo stopped') # last mesage
    print('done')
