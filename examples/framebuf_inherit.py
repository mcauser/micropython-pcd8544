# Inherting the framebuffer

import pcd8544_fb
from machine import Pin, SPI

spi = SPI(1)
spi.init(baudrate=2000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(12, Pin.OUT, value=1)

lcd = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)

lcd.text('Hello', 0, 0, 1)
lcd.pixel(30, 30, 1)
lcd.pixel(31, 31, 1)
lcd.pixel(32, 32, 1)
lcd.pixel(33, 33, 1)
lcd.pixel(34, 34, 1)
lcd.hline(0, 20, 8, 1)
lcd.vline(30, 8, 8, 1)
lcd.rect(40, 16, 8, 8, 1)
lcd.fill_rect(16, 32, 8, 8, 1)
lcd.show()
