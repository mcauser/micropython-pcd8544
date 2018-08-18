# Extending PCD8544 with Framebuf methods

import pcd8544
from machine import Pin, SPI

spi = SPI(1)
spi.init(baudrate=2000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(12, Pin.OUT, value=1)

lcd = pcd8544.PCD8544_FRAMEBUF(spi, cs, dc, rst)

# fill(color)
lcd.fill(1)
lcd.show()

# text(string, x, y, color)
lcd.fill(0)
lcd.text('Nokia 5110', 0, 0, 1)
lcd.text('PCD8544', 0, 10, 1)
lcd.text('84x48', 0, 20, 1)
lcd.text('uPython1.9', 0, 30, 1)
lcd.text('ESP8266', 0, 40, 1)
lcd.show()
