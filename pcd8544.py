# MicroPython PCD8544 84x48 LCD driver, eg Nokia 5110 LCD.

from micropython import const
from ustruct import pack
from utime import sleep_us

# Function set 0010 0xxx
FUNCTION_SET     = const(0x20)
POWER_DOWN       = const(0x04)
ADDRESSING_VERT  = const(0x02)
EXTENDED_INSTR   = const(0x01)

# Display control 0000 1x0x
DISPLAY_BLANK    = const(0x08)
DISPLAY_ALL      = const(0x09)
DISPLAY_NORMAL   = const(0x0c)
DISPLAY_INVERSE  = const(0x0d)

# Temperature control 0000 01xx
TEMP_COEFF_0     = const(0x04)
TEMP_COEFF_1     = const(0x05)
TEMP_COEFF_2     = const(0x06) # default
TEMP_COEFF_3     = const(0x07)

# Bias system 0001 0xxx
BIAS_1_100       = const(0x10)
BIAS_1_80        = const(0x11)
BIAS_1_65        = const(0x12)
BIAS_1_48        = const(0x13)
BIAS_1_40        = const(0x14) # default
BIAS_1_24        = const(0x15)
BIAS_1_18        = const(0x16)
BIAS_1_10        = const(0x17)

# Set operation voltage
SET_VOP          = const(0x80)

# DDRAM addresses
COL_ADDR         = const(0x80) # x pos (0~83)
BANK_ADDR        = const(0x40) # y pos, in banks of 8 rows (0~5)

class PCD8544:
	def __init__(self, spi, cs, dc, rst=None):
		self.width  = 84
		self.height = 48

		self.spi    = spi
		self.cs     = cs   # chip enable, active LOW
		self.dc     = dc   # data HIGH, command LOW
		self.rst    = rst  # reset, active LOW

		self.cs.init(self.cs.OUT, value=1)
		self.dc.init(self.dc.OUT, value=0)

		if self.rst:
			self.rst.init(self.rst.OUT, value=1)
		self.reset()
		self.init()

	def init(self, horizontal=True, contrast=0x3f, bias=BIAS_1_40, temp=TEMP_COEFF_2):
		# power up, horizontal addressing, basic instruction set
		self.fn = FUNCTION_SET

		# switch to vertical addressing
		if not horizontal:
			self.fn |= ADDRESSING_VERT

		self.contrast(contrast, bias, temp)
		self.cmd(DISPLAY_NORMAL)
		self.clear()

	def reset(self):
		# issue reset impulse to reset the display
		self.rst(1)
		sleep_us(100)
		self.rst(0)
		sleep_us(100) # reset impulse has to be >100 ns and <100 ms
		self.rst(1)
		sleep_us(100)

	def power_on(self):
		self.cs(1)
		self.fn &= ~POWER_DOWN
		self.cmd(self.fn)

	def power_off(self):
		self.fn |= POWER_DOWN
		self.cmd(self.fn)

	def contrast(self, contrast=0x3f, bias=BIAS_1_40, temp=TEMP_COEFF_2):
		for cmd in (
			# extended instruction set is required to set temp, bias and vop
			self.fn | EXTENDED_INSTR,
			# set temperature coefficient
			temp,
			# set bias system (n=3 recommended mux rate 1:40/1:34)
			bias,
			# set contrast with operating voltage (0x00~0x7f)
			# 0x00 = 3.00V, 0x3f = 6.84V, 0x7f = 10.68V
			# starting at 3.06V, each bit increments voltage by 0.06V at room temperature
			SET_VOP | contrast,
			# revert to basic instruction set
			self.fn & ~EXTENDED_INSTR):
			self.cmd(cmd)

	def invert(self, invert):
		self.cmd(DISPLAY_INVERSE if invert else DISPLAY_NORMAL)

	def clear(self):
		# clear DDRAM, reset x,y position to 0,0
		self.data([0] * (self.height * self.width // 8))
		self.position(0, 0)

	def position(self, x, y):
		# set cursor to column x (0~83), bank y (0~5)
		self.cmd(COL_ADDR | x) # set x pos (0~83)
		self.cmd(BANK_ADDR | y) # set y pos (0~5)

	def cmd(self, command):
		self.dc(0)
		self.cs(0)
		self.spi.write(bytearray([command]))
		self.cs(1)

	def data(self, data):
		self.dc(1)
		self.cs(0)
		self.spi.write(pack('B'*len(data), *data))
		self.cs(1)
