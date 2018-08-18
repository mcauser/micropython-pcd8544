# Sine waves

import time
import math

import pcd8544_fb
from machine import Pin, SPI

spi = SPI(1)
spi.init(baudrate=2000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(12, Pin.OUT, value=1)

lcd = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)


def draw_sin(amplitude, freq, phase, yoffset=24):
	for i in range(freq):
		y = int((math.sin((i + phase) * 0.017453) * amplitude) + yoffset)
		x = int((84 / freq) * i)
		lcd.pixel(x, y, 1)
	lcd.show()

def draw_cos(amplitude, freq, phase, yoffset=24):
	for i in range(freq):
		y = int((math.cos((i + phase) * 0.017453) * amplitude) + yoffset)
		x = int((84 / freq) * i)
		lcd.pixel(x, y, 1)
	lcd.show()


# big wave
lcd.fill(0)
draw_sin(20, 360, 0)

# little wave
lcd.fill(0)
draw_sin(10, 5*360, 0)

# tiny wave
draw_sin(5, 10*360, 0)

# two waves
lcd.fill(0)
draw_sin(10, 4*360, 0, 12*1)
draw_cos(10, 4*360, 0, 12*3)

# three waves
lcd.fill(0)
draw_sin(20, 360, 0)
draw_sin(15, 2*360, 30)
draw_sin(10, 4*360, 60)

# lots of waves
lcd.fill(0)
for i in range(0,360,30):
	draw_sin(20, 360, i)
