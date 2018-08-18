# QR Code
# You'll have to scan it to find out what it is.

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
fbuf = framebuf.FrameBuffer(buffer, pcd8544.WIDTH, pcd8544.HEIGHT, framebuf.MONO_VLSB)

fbuf.fill(0)

# QR Code - col major msb
# See qr-code.gif
qr = bytearray(b'\x7F\x41\x5D\x5D\x5D\x41\x7F\x00\xF6\x1A\xF3\x80\x70\x38\xEB\xB7\x60\x00\x7F\x41\x5D\x5D\x5D\x41\x7F\x47\x8B\xA4\xF5\x96\xF6\x55\x89\x98\x8A\x18\xCB\x72\x9B\x73\x00\xD3\x1E\x7B\x79\xC5\x30\x61\x95\x76\xFD\x05\x74\x75\x75\x04\xFD\x01\xA6\xBD\x96\x91\xBA\xD6\x68\x4F\x9F\xD1\x15\x71\x7F\xBF\x69\x0C\x46\x01\x01\x01\x01\x01\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x01\x01\x00\x01\x01\x00\x00\x00\x01\x01')
qr_fbuf = framebuf.FrameBuffer(qr, 25, 25, framebuf.MONO_VLSB)

fbuf.blit(qr_fbuf, int((pcd8544.WIDTH-25)/2), int((pcd8544.HEIGHT-25)/2), 0)

lcd.clear()
lcd.data(buffer)
