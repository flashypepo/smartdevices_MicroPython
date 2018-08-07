# LDR35 light  sensor
# lightsensor is in a voltage divider circuit
# Ucc = 1.6 V
# Uout = Ucc (R/R+Rldr), R=10k
# Ucc is generated form another voltage divider, 2x R=10k
# 2017-0808 PePo adopted for NodeMCU

import machine, time

_ADC_PIN = const(0)
_WARNING_LED_PIN = const(14) # Huzzah

# program
# read ADC-value
adc = machine.ADC(_ADC_PIN)
#TEST: print('ADC reading:', adc.read())
alert = machine.Pin(_WARNING_LED_PIN, machine.Pin.OUT)

# Ucc = 1.6 volt
#_UREF = 1.6 #3.3 NodeMCU, Huzzah: 1.6 # Ucc in circuit
_UREF = 1.0 #3.3 NodeMCU, Huzzah: 1.6 # Ucc in circuit
def adc2voltage(value):
    # Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    return value * (_UREF / 1024.0)

# run readng T, Ctrl-C to abort
def run(dt=2.5):
    while True:
        reading = adc.read()
        voltage = adc2voltage(reading)
        print('Photocell reading {0}\tvoltage {1:0.1f}'.format(reading, voltage))
        if reading > 1000:
            alert.value(1)
        else:
            alert.value(0)
        time.sleep(dt) #wait > s, see datasheet

#execute
try:
    run()
except:
    print ('Interrupted, done!')
