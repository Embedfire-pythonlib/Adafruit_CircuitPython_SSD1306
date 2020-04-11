# Basic example of clearing and drawing pixels on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Tony DiCola
# License: Public Domain

# Import all board pins.
import time
import random

from board import SCL, SDA, DC, RST, SS0
import busio
import board
import digitalio

# Import the SSD1306 module.
import adafruit_ssd1306

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


# # Create the SPI interface.
# spi = board.SPI()
# oled_cs = digitalio.DigitalInOut(SS0)
# oled_dc = digitalio.DigitalInOut(DC)
# oled_reset = None
# display = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, oled_dc, oled_reset, oled_cs)

# Alternatively you can change the I2C address of the device with an addr parameter:
#display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
display.show()

for x in range(0, 127):
    for y in range(0, 63):
        display.pixel(int(random.uniform(0, 127)), int(random.uniform(0, 63)), 1)
        display.show()
        # time.sleep(0.01)

# Set a pixel in the origin 0,0 position.
# display.pixel(0, 0, 1)
# # Set a pixel in the middle 64, 16 position.
# display.pixel(64, 16, 1)
# # Set a pixel in the opposite 127, 31 position.
# display.pixel(127, 31, 1)
# display.pixel(127, 32, 1)
# display.show()
