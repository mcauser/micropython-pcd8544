# Load a remote image with urequests

# You need to be connected to the internet to fetch the image
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect('SSID', 'PASSWORD') # change me


# Install urequests with upip, or simply copy the file to your board
import urequests

import pcd8544
from machine import Pin, SPI

spi = SPI(1)
spi.init(baudrate=2000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(12, Pin.OUT, value=1)

lcd = pcd8544.PCD8544(spi, cs, dc, rst)

lcd.init()

# fetch remote image and display
# image is 84x48 pixels, 504 bytes, in horizontal address format
# see wemos.gif
r = urequests.get('http://202.4.227.150/wemos.dat')
lcd.data(r.content)
r.close()
