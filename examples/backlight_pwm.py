# Backlight PWM

import pcd8544
from machine import Pin, SPI, PWM

spi = SPI(1)
spi.init(baudrate=2000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)

# backlight on
bl = Pin(12, Pin.OUT, value=1)

# backlight dimming
bl_pwm = PWM(bl)
bl_pwm.freq(500)
bl_pwm.duty(0)    # off
bl_pwm.duty(512)  # dim
bl_pwm.duty(1024) # bright

lcd = pcd8544.PCD8544(spi, cs, dc, rst)

# test pattern (50% on)
lcd.data(bytearray([0x55, 0xAA] * 42 * 6))
