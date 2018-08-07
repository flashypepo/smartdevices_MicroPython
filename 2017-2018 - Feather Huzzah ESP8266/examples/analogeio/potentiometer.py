# potentiometer.py: reading potentiometer values from ADC-port of ESP8266
# Note: use a voltage divider becasue vlotage at ADC-pin MUST not exceed 1.0V
# 2017-0925 PePo new, Huzzah

import machine, time

# create an ADC object
adc = machine.ADC(0) # channel must be 0

# function to get volt values from ADC
def getADC():
    reading = adc.read() # read raw data from ADC
    data = reading / 2**10 # convert to mV, ADC resolution is 2**10 (0..1024)
    #print('ADC: reading={0}, data={1} V'.format(reading, data))
    return data

# function to keep reading values from ADC
def run(dt=2):
    try:
        while True:
            data = getADC()
            print('ADC data=', data)
            #print('ADC: data={0:06.2f} V'.format(data))
            time.sleep(dt)
    except:
        print('done')

#create led-object at GPIO14
led = machine.Pin(14, machine.Pin.OUT)
led.value(0)
def demoLED():
    try:
        while True:
            data = getADC()
            print('ADC: data={0:04.2f} V'.format(data))
            #print('ADC data=', data)
            led.value(1)
            time.sleep(data)
            led.value(0)
            time.sleep(data)
    except:
        print('done')

# execute
#run()
demoLED()
