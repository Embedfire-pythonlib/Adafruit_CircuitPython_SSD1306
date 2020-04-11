# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
import board
import busio
from board import SCL, SDA, DC, RST, SS0
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
# RESET_PIN = digitalio.DigitalInOut(board.D4)


# # Create the I2C interface.
# i2c = busio.I2C(SCL, SDA)
# oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


# Create the SPI interface.
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(SS0)
oled_dc = digitalio.DigitalInOut(DC)
oled_reset = None
oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, oled_dc, oled_reset, oled_cs)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new('1', (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
# font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
# font2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)

# Load default font.
font = ImageFont.load_default()

# Draw the text
draw.text((0, 0), 'Hello!', font=font, fill=255)
draw.text((0, 20), 'embedfire!', font=font, fill=255)
draw.text((34, 46), 'NXP-imx6ull!', font=font, fill=255)

# Display image
oled.image(image)
oled.show()
