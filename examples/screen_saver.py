# Screen Saver
# Move a bitmap around, bounce it off walls like an old screensaver

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

# smiley 15x15 - col major msb
smiley = bytearray(b'\xE0\x38\xE4\x22\xA2\xE1\xE1\x61\xE1\x21\xA2\xE2\xE4\x38\xE0\x03\x0C\x10\x21\x21\x41\x48\x48\x48\x49\x25\x21\x10\x0C\x03')
smiley_w = 15
smiley_h = 15
smiley_fbuf = framebuf.FrameBuffer(smiley, smiley_w, smiley_h, framebuf.MONO_VLSB)

# area the smiley can move in
bounds_w = pcd8544.WIDTH - smiley_w
bounds_h = pcd8544.HEIGHT - smiley_h

# direction smiley is moving
move_x = 1
move_y = 1

# pause between displaying frames
from time import sleep_ms
pause = 100

# start position
x = 1
y = 1

def render():
	global x
	global y
	global move_x
	global move_y
	# Draw the bitmap
	fbuf.fill(0)
	fbuf.blit(smiley_fbuf, x, y, 0)
	lcd.data(buffer)

	sleep_ms(pause)

	# Move down right until hit bounds
	# Then flip increment to decrement to bounce off the wall
	x = x + move_x
	y = y + move_y
	if (x <= 0 or x >= bounds_w):
		move_x = -move_x
	if (y <= 0 or y >= bounds_h):
		move_y = -move_y

while(True):
	render()
