# demo DC motor on port GPIO15
# show motor duty on OLED on I2C
# 2017-1009 PePo new

# DO: type in the Python code in REPL, line by line.

import machine, time, ssd1306

# motor object
GPIO_MOTOR = 12 #Huzzah: GPIO12
pin_motor = machine.Pin(GPIO_MOTOR, machine.Pin.OUT)
motor = machine.PWM(pin_motor)

MOTOR_MIN = 0  # minimum duty
MOTOR_MAX  = 1023 # maximum duty

# OLED on I2C
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
#i2c = I2C(scl=Pin(SCL), sda=Pin(SDA), freq=100000)
#i2c.scan()   #[60]
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# OLED helper function: erse OLED screen
def erase():
    oled.fill(0)
    oled.show()

# Motor function: slowly turn on the motor
def motorOn(oled, d1=MOTOR_MIN, d2=MOTOR_MAX, step=1, dt=0.01):
    for i in range(d1, d2, step):
        motor.duty(i)

        oled.fill(0)
        oled.text('duty: {0}'.format(motor.duty()), 0, 0)
        oled.show()

        time.sleep(dt)

# Motor function: slowly turn off the motor
def motorOff(oled, d1=MOTOR_MAX, d2=MOTOR_MIN, step=-1, dt=0.01):
    for i in range(d1, d2, step):
        motor.duty(i)

        oled.fill(0)
        oled.text('duty: {0}'.format(motor.duty()), 0, 0)
        oled.show()

        time.sleep(dt)

def motorStop(oled):
    motor.duty(0);

    oled.fill(0) # erase OLED
    oled.text('duty: {0}'.format(motor.duty()), 0, 0)
    oled.show()

# demo
def run():
    motorStop(oled) # stop motor
    time.sleep(0.5)

    print('turn motor on ...')
    motorOn(oled)   # turn motor on
    time.sleep(1)   # wait

    print('turn motor off ...')
    motorOff(oled)  # turn motor off
    motorStop(oled) # stop motor
    print('motor stopped ...')

# execute ...
run()
