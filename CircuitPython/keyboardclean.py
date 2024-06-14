# Matrix Keypad
# NerdCave - https://www.youtube.com/channel/UCxxs1zIA4cDEBZAHIJ80NVg - Subscribe if you found this helpful.
# Github - https://github.com/Guitarman9119

import board
import digitalio
import time
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# Create a map between keypad buttons and characters
matrix_keys = [['Q', 'W', 'E', 'R'],
               ['4', '5', '6', 'B'],
               ['7', '8', '9', 'C'],
               ['*', '0', '#', 'D']]

# PINs according to schematic - Change the pins to match with your connections
keypad_rows = [board.GP5, board.GP4, board.GP3, board.GP2]
keypad_columns = [board.GP9, board.GP8, board.GP7, board.GP6]

# Create two empty lists to set up pins (Rows output and columns input)
col_pins = []
row_pins = []

# Loop to assign GPIO pins and setup input and outputs
for pin in keypad_rows:
    row_pin = digitalio.DigitalInOut(pin)
    row_pin.direction = digitalio.Direction.OUTPUT
    row_pin.value = False
    row_pins.append(row_pin)

for pin in keypad_columns:
    col_pin = digitalio.DigitalInOut(pin)
    col_pin.direction = digitalio.Direction.INPUT
    col_pin.pull = digitalio.Pull.DOWN
    col_pins.append(col_pin)

############################## Scan keys ####################

print("Please enter a key from the keypad")

def scankeys():  
    for row in range(4):
        row_pins[row].value = True
        for col in range(4):
            if col_pins[col].value:
                key = matrix_keys[row][col]
                if key == 'Q':                    
                    kbd.press(Keycode.Q)
                    time.sleep(0.2)
                    kbd.release(Keycode.Q)
                if key == 'W':                    
                    kbd.press(Keycode.W)
                    time.sleep(0.2)
                    kbd.release(Keycode.W)
                if key == 'E':                    
                    kbd.press(Keycode.E)
                    time.sleep(0.2)
                    kbd.release(Keycode.E)
                if key == 'R':                    
                    kbd.press(Keycode.R)
                    time.sleep(0.2)
                    kbd.release(Keycode.R)
                print("You have pressed:", matrix_keys[row][col])
        row_pins[row].value = False

while True:
    scankeys()