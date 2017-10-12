# demo DC motor on port GPIO15
# source: https://github.com/nickzoic/mpy-tut/blob/master/motors.rst
# 2017-1008 PePo test on ESP32 - yellow pins

# DO: type in the Python code in REPL, line by line.

import machine, time

# The motor can be driven at different speeds by varying
# the duty cycle, just like with the LED. So it's using PWM.
GPIO_MOTOR = 12 #Huzzah: 12
pin_motor = machine.Pin(GPIO_MOTOR, machine.Pin.OUT)
motor = machine.PWM(pin_motor)
print('Motor duty=', motor.duty())
# waarde is 512

#DO: motor.duty(0) # stop motor
#motor.duty(1023) # motor full-speed

# slowly turn on the motor
# DO: change 0.01 to, for example, 0.1, what happens?
for i in range(1023):
    motor.duty(i)
    time.sleep(0.01)

time.sleep(3)

#slowly turn down the motor
# DO: change 0.01 to, for example, 0.1, what happens?
for i in range(1023,0,-1):
     motor.duty(i)
     time.sleep(0.01)
