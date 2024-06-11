import touchio
import board
import pwmio
import usb_hid
import time


import analogio

import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

touchPin = board.GP18
touch = touchio.TouchIn(touchPin)
mouse = Mouse(usb_hid.devices)

#Set up PWM on GP21
led = pwmio.PWMOut(board.GP21, frequency=5000, duty_cycle=0)

#Function to set LED brightness
def set_brightness(brightness):
    # Brightness should be a value between 0 (off) and 65535 (full brightness)
    led.duty_cycle = brightness

while True:
    if touch.value:
        set_brightness(int(65534 *0.9))  # 50% brightness
        mouse.move(x=20)
    else:
        set_brightness(65534)
    #print("Touch: ", str(touch.value))
    time.sleep(0.001)