# demo temperatuur sensor DHT22
# Configuration:
# - temperature/humidity sensor DHT22 on GPIO12
# - lED op GPIO14
# 2017-1003 PePo OLED output, Huzzah

import machine,time
import dht
import ssd1306

# create DHT22 sensor object
sensor = dht.DHT22(machine.Pin(12))

# create LED object on pin GPIO14
led = machine.Pin(14, machine.Pin.OUT)
#led.value(0)

# create i2c object: SCL=pin 5, SDA=pin 4
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
i2c.scan()   #test -> [60], dan OLED correct aangesloten

# create I2C OLED object: 128 * 32 pixels
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
oled.fill(0) # blank oleD
oled.show()

# demo - led=on when Humidity > h_threshold
def run(threshold = 80, dt=2.5):
    # get sensor data
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()

    #console: print('T:{0} Celsius, H:{1} %'.format(t, h ))
    # display sensor data on OLED
    oled.text('Sensor DHT22',0, 0)
    oled.text('T {0:0.1f} Celsius'.format(t),0, 10)
    oled.text('H {0:0.1f} %'.format(h),0, 20)
    oled.show()

    # check threshold
    if h > threshold:
        led.value(1)
        print('Alert!')
    else:
        led.value(0)

    # wait between measurements
    # time delay must be at least 2 seconds for sensor
    time.sleep(dt)

#execute
try:
    while True:
        # blank oleD
        oled.fill(0)
        oled.show()
        run()
except:
    # blank oleD
    oled.fill(0)
    oled.show()
    print('demo done!')
