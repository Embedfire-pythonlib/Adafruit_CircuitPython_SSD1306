import time
import digitalio
from board import BEEP

beep = digitalio.DigitalInOut(BEEP)
beep.switch_to_output()

while True:
    beep.value = 0
    time.sleep(1)
    beep.value = 1
    time.sleep(1)
