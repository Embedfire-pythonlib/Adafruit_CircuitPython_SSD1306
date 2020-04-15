import time
import digitalio
from board import BUTTON

button = digitalio.DigitalInOut(BUTTON)
button.switch_to_input()

print("please touch the button!")

while True:
    if (button.value):
        print("the button is pressed...")
        time.sleep(1)
