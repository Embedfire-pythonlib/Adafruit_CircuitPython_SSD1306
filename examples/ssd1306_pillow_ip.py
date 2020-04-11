# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
import socket
import fcntl
import struct
from board import SCL, SDA, DC, RST, SS0
import busio
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# This function allows us to grab any of our IP addresses
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', str.encode(ifname[:15]))
    )[20:24])

# Setting some variables for our reset pin etc.
# RESET_PIN = digitalio.DigitalInOut(board.D4)
TEXT = ''

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
# i2c = board.I2C()
# oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3d, reset=RESET_PIN)

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


# # Create the SPI interface.
# spi = board.SPI()
# oled_cs = digitalio.DigitalInOut(SS0)
# oled_dc = digitalio.DigitalInOut(DC)
# oled_reset = None
# oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, oled_dc, oled_reset, oled_cs)

# This sets TEXT equal to whatever your IP address is, or isn't
try:
    TEXT = get_ip_address('wlan0') # WiFi address of WiFi adapter. NOT ETHERNET
except IOError:
    try:
        TEXT = get_ip_address('eth1') # WiFi address of Ethernet cable. NOT ADAPTER
    except IOError:
        try:
            TEXT = get_ip_address('eth2') # WiFi address of Ethernet cable. NOT ADAPTER
        except IOError:
            TEXT = ('NO INTERNET!')

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
intro = 'Hello!'
ip = 'Your IP Address is:'
draw.text((0, 46), TEXT, font=font, fill=255)
draw.text((0, 0), intro, font=font, fill=255)
draw.text((0, 30), ip, font=font, fill=255)

# Display image
oled.image(image)
oled.show()
