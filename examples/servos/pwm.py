# PWM voorbeeld - fading led on GPIO15
# PWM only on pins  0, 2, 4, 5, 12, 13, 14 and 15
# URL: http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/pwm.html
# 2017-1011 PePo LED op GPIO15

import machine, time
import math

# led object for LED on GPIO15
led = machine.PWM(machine.Pin(15, machine.Pin.OUT))

# pulse: pulses the led by means of PWM and sin
def pulse(led, t):
     for i in range(20):
         led.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
         time.sleep_ms(t)

# run
import urandom
def run():
    try:
        counter = 0
        dt = urandom.getrandbits(7)
        #print('dt:', dt)
        while True:
            counter = counter + 1
            # get random number between 0 and 2**7 (=128)
            # every 10 times to make pulsing less erratic
            if counter > 10:
                counter = 0
                dt = urandom.getrandbits(7)
                #print('dt:', dt)
                pulse(led, dt)
    except:
        #led.deinit()
        print('done!')

# execute
run()
