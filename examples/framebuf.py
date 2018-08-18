# Using the MicroPython 1.9 framebuffer

import pcd8544
from machine import Pin, SPI

spi = SPI(1)
spi.init(baudrate=2000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(12, Pin.OUT, value=1)

lcd = pcd8544.PCD8544(spi, cs, dc, rst)

import framebuf
buffer = bytearray((pcd8544.HEIGHT // 8) * pcd8544.WIDTH)
framebuf = framebuf.FrameBuffer(buffer, pcd8544.WIDTH, pcd8544.HEIGHT, framebuf.MONO_VLSB)

# fill(color)
framebuf.fill(1)
lcd.data(buffer)

# text(string, x, y, color)
framebuf.fill(0)
framebuf.text('Nokia 5110', 0, 0, 1)
framebuf.text('PCD8544', 0, 10, 1)
framebuf.text('84x48', 0, 20, 1)
framebuf.text('uPython1.9', 0, 30, 1)
framebuf.text('ESP8266', 0, 40, 1)
lcd.data(buffer)

# pixel(x, y, colour)
framebuf.fill(0)
framebuf.pixel(0, 0, 1)
framebuf.pixel(0, 2, 1)
framebuf.pixel(2, 0, 1)
framebuf.pixel(2, 2, 1)
lcd.data(buffer)

# line(x1, y1, x2, y2, color)
framebuf.fill(0)
framebuf.line(0, 47, 83, 0, 1)
framebuf.line(83, 47, 0, 0, 1)
lcd.data(buffer)

# hline(x, y, w, color)
framebuf.fill(0)
framebuf.hline(0, 10, 20, 1)
framebuf.hline(0, 20, 41, 1)
framebuf.hline(0, 30, 62, 1)
framebuf.hline(0, 40, 83, 1)
lcd.data(buffer)

# vline(x, y, h, color)
framebuf.fill(0)
framebuf.vline(10, 0, 11, 1)
framebuf.vline(20, 0, 23, 1)
framebuf.vline(30, 0, 35, 1)
framebuf.vline(40, 0, 47, 1)
lcd.data(buffer)

# rect(x, y, w, h, c)
framebuf.fill(0)
framebuf.rect(0, 0, 20, 20, 1)
framebuf.rect(10, 10, 20, 20, 1)
framebuf.rect(20, 20, 20, 20, 1)
lcd.data(buffer)

# fill_rect(x, y, w, h, c)
framebuf.fill(0)
framebuf.fill_rect(0, 0, 20, 20, 1)
framebuf.fill_rect(20, 20, 20, 20, 1)
framebuf.fill_rect(10, 10, 20, 20, 0)
lcd.data(buffer)
