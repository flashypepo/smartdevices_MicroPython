# demo#1 servo motor: showing PWM
# servo is connected to GPIO14
# DHT22 is connected to GPIO12
# 2017-1008 PePo demo for college #6

import machine, time
import servo
# Notice: module servo.py on Smartworld >> SmartDevices
# It's a modified servo module from DiCola: extended with deinit()

# create servo object - default arguments
sv_pin = machine.Pin(14, machine.Pin.OUT) #Huzzah: Servo op GPIO14
sv = servo.Servo(sv_pin)
time.sleep(1)

# ################### PART 1 ######################
#''' part 1: sweep servo between 0 en 180 degrees, and back
try:
    while True:
        sv.write_angle(0)
        time.sleep(2)
        sv.write_angle(180)
        time.sleep(2)
except:
  sv.deinit()
  print('done!')
  
#'''

# ################### PART 2 ######################
''' part 2: sweep servo at slower speed from angle 0 to 180 and back
# sweep servo s from angle 0 to 180
print('go...')
for i in range(0, 180):
    print('angle: ', i)
    sv.write_angle(i)
    time.sleep(0.2)

time.sleep(2)

print('and back...')
for i in range(180, 0, -1):
    print('angle: ', i)
    sv.write_angle(i)
    time.sleep(0.2)
#'''

# ################### PART 3 ######################
''' part 3: functions to move servo forward and backward
# move servo forwards: increase angle
def forward(s, p1 = 0, p2 = 180, dt=0.1):
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

# demo function: move servo s from 0 to 180 and back
def demo(s):
    forward(s)
    time.sleep(2)
    backward(s)

# run...
try:
    while True:
        demo(sv)
except:
    sv.deinit() #de-couple PWM from GPIO
    print('done')
#'''
