#!/usr/bin/python3

import Adafruit_BBIO.SPI as SPI
from Adafruit_BBIO.SPI import SPI


spi = SPI(0,0)
spi.open(0,0)

while True:
  # go through the six channels of the digital pot:
  for channel in range (0,6):
    # change the resistance on this channel from min to max:
    for level in range(0,255):
      digitalPotWrite(channel, level)
      delay(10)
    
    # wait a second at the top:
    delay(100)
    # change the resistance on this channel from max to min:
    for level in range(0,255):
      digitalPotWrite(channel, 255 - level)
      delay(10)

def digitalPotWrite(address, value):
  # take the SS pin low to select the chip:
  cshigh = False
  delay(100)
  # send in the address and value via SPI:
  spi.xfer2([address])
  spi.xfer2([value])
  delay(100)
  # take the SS pin high to de-select the chip:
  cshigh = True

