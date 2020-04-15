import time
import digitalio
from board import R_LED, G_LED, B_LED

rled = digitalio.DigitalInOut(R_LED)
gled = digitalio.DigitalInOut(G_LED)
bled = digitalio.DigitalInOut(B_LED)

rled.switch_to_output()
gled.switch_to_output()
bled.switch_to_output()

while True:
    rled.value = 0
    time.sleep(1)
    rled.value = 1
    gled.value = 0
    time.sleep(1)
    gled.value = 1
    bled.value = 0
    time.sleep(1)
    bled.value = 1
    time.sleep(1)