# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
import time
import board
from board import SCL, SDA, DC, RST, SS0
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
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

# Create blank image for drawing.
image = Image.new('1', (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.load_default()

offset = 0 # flips between 0 and 32 for double buffering

while True:
    # write the current time to the display after each scroll
    draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
    text = time.strftime("%A")
    draw.text((0, 0), text, font=font, fill=255)
    text = time.strftime("%e %b %Y")
    draw.text((0, 14), text, font=font, fill=255)
    text = time.strftime("%X")
    draw.text((0, 36), text, font=font, fill=255)
    oled.image(image)
    oled.show()

    time.sleep(1)

    for i in range(0, oled.height//2):
        offset = (offset + 1) % oled.height
        oled.write_cmd(adafruit_ssd1306.SET_DISP_START_LINE | offset)
        oled.show()
        time.sleep(0.001)
