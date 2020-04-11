# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
import sys
from board import SCL, SDA, DC, RST, SS0
import busio
import board
import digitalio
from PIL import Image
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# # Create the SPI interface.
# spi = board.SPI()
# oled_cs = digitalio.DigitalInOut(SS0)
# oled_dc = digitalio.DigitalInOut(DC)
# oled_reset = None
# oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, oled_dc, oled_reset, oled_cs)

# Clear display.
oled.fill(0)
oled.show()

# Open, resize, and convert image to Black and White
image = Image.open(sys.argv[1]).resize((oled.width, oled.height), Image.BICUBIC).convert('1')

# Display the converted image
oled.image(image)
oled.show()
