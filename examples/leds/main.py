# main.py for SmartDevices demos
# digitalio, analogio, i2c/OLED, actuators, weahterstation
# 2017-0904 OLED demo  for kickoff
# 2017-0808 PePo added button (GPIO12)
# 2017-0805 PePo added LDR35 (ADC)
# 2017-0728 PePo new TMP36 (ADC)

# ----- digitalIO examples -------
#'''
import digitalio.pulsebuiltinLED
#import digitalio.blinkingLED
#import digitalio.pulseLED
#import digitalio.button
#import digitalio.buttonLED
#'''

# ----- analogIO examples -------
#''' tmp36 experiment
#import temperature.tmp36 #zonder OLED
#import temperature.tmp36_oled
# LDR35 experiment
import light.ldr  #zonder OLED
#import light.ldr_oled
#'''

''' ----- DHT22 examples -------
# GPIO5, LED on GPIO14
import temperature.dht22
#'''

''' LDR35 experiment
import light.ldr_oled
#'''

''' OLED demo, used as test for displays
import oledssd1306
#'''

''' Button / interrupt experiment
#import button.demo
import button.demo_oled
#import button.demo_oled_interrupt
#'''
