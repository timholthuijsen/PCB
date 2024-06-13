import touchio
import board
import pwmio
import usb_hid
import time


import analogio

import digitalio
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize Keyboard
kbd = Keyboard(usb_hid.devices)

touchPin = board.GP18
touch = touchio.TouchIn(touchPin)
mouse = Mouse(usb_hid.devices)

#Set up PWM on GP21
led = pwmio.PWMOut(board.GP21, frequency=5000, duty_cycle=0)

#Set up external led pin
external_led_pin = board.GP6
external_led = DigitalInOut(external_led_pin)
external_led.direction = Direction.OUTPUT
external_led.value = True

button_pin = board.GP15
button = DigitalInOut(button_pin)
button.direction = Direction.INPUT
button.pull = Pull.UP

#Function to set LED brightness
def set_brightness(brightness):
    # Brightness should be a value between 0 (off) and 65535 (full brightness)
    led.duty_cycle = brightness

while True:

    if touch.value:
        set_brightness(int(65535 *0.5))  # 50% brightness
        print('the rapsberry is printing this')
        #kbd.press(Keycode.A)
        time.sleep(0.1)
        kbd.release(Keycode.A)
        external_led.value = False
        print(button.value)
        #mouse.move(x=20)
    else:
        set_brightness(65534)
        external_led.value = True