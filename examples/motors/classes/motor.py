'''
 MicroPython Motor driver for the SmartDevices.
 The motor is PWM-controlled, attached to 1 GPIO, no directions.
 Author: Peter van der Post
 License: Public Domain

 Configuration
    GPIO12   motor   input  adjust speed by PWM
 Battery: 5V / TODO: test LiPo 1200mAH, 4.2V
'''
import machine

class Motor:
    '''
     Make a Motor class for the motor
     '''
    # creates Motor object on GPIOs gpiom and gpiod, freq=1000 by-default
    def __init__(self, gpiom, gpiod = None, freq = 1000):
        # motor Pins - PWM controlled
        # freq=100 seems to work, duty=0: motor off
        self._freq = freq
        self._motor = machine.PWM(machine.Pin(gpiom), freq=self._freq, duty=0)
        # direction pins - 2017-1009 NOT PRESENT
        #self._direction = machine.Pin(gpiod, machine.Pin.OUT)
        # re-set Motor-object
        self._reset()

        # re-sets the motor: speed=0, forward direction
    def _reset(self):
        self._speed = 0 #range: 0..1023
        self._forward = 1
        #NOT PRESENT: self._direction = None #.on()

    def freq(self):
        return self._freq

    # brake() - motors off
    def brake(self):
        self._motor.duty(0)
        self._reset()

    # set speed of motor
    def speed(self, value=None):
        print('\tDEBUG: speed({0}) called'.format(value))
        if value is None:
            # get current duty value
            value = self._motor.duty()
        elif value > 0:
            # forward
            self._forward = 1
            #self._direction.on()
            #print('\tDEBUG: forward=', self._forward)

        ''' next statements are not relevant with one motor
            and no direction
        elif value < 0:
            # backward
            self._forward = -1
            #self._direction.off()
            #print('\tDEBUG: forward=', self._forward)
        else:
            # release
            print('\tTODO: release - what TODO ?')
            self._forward = 0
            #print('\tDEBUG: forward=', self._forward)
            pass
        #'''
        # motor is on
        print('\tDEBUG: motor.duty=', abs(value))
        self._motor.duty(abs(value))
        return abs(value) #PePo 2017-1009

        # PePo new 2017-1009
    def deinit(self):
        print('\tDEBUG: deinit motor')
        self._motor.deinit()
