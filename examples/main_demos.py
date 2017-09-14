# main.py for testing OLED-displays and sensors
# 2017-0904 OLED demo  for kickoff
# 2017-0808 PePo added button (GPIO12)
# 2017-0805 PePo added LDR35 (ADC)
# 2017-0728 PePo new TMP36 (ADC)

#''' OLED demo, used as test for displays
import oledssd1306
#'''

''' tmp36 experiment
#import temperature.tmp36 #zonder OLED
import temperature.tmp36_oled
#'''

''' LDR35 experiment
import light.ldr_oled
#'''

''' Button / interrupt experiment
#import button.demo
import button.demo_oled
#import button.demo_oled_interrupt
#'''
