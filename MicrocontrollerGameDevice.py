import time
import board
import digitalio
import analogio
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Define constants for mouse control
POT_MIN = 0.00
POT_MAX = 3.29
STEP = (POT_MAX - POT_MIN) / 20.0
MOUSE_THRESHOLD_LOW = 9.0
MOUSE_THRESHOLD_MEDIUM = 15.0
MOUSE_THRESHOLD_HIGH = 19.0
MOUSE_STEP_LOW = 1
MOUSE_STEP_MEDIUM = 15
MOUSE_STEP_HIGH = 25

# Setup mouse
mouse = Mouse(usb_hid.devices)
x_axis = analogio.AnalogIn(board.GP27)
y_axis = analogio.AnalogIn(board.GP26)
select = digitalio.DigitalInOut(board.GP16)
select.direction = digitalio.Direction.INPUT
select.pull = digitalio.Pull.UP

# Setup keyboard
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

def get_voltage(pin):
    voltage = (pin.value * 3.3) / 65536
    return voltage

def steps(axis):
    """ Maps the potentiometer voltage range to 0-20 """
    return round((axis - POT_MIN) / STEP)

def calculate_movement(axis_steps):
    """ Calculates movement based on the step value """
    if axis_steps > MOUSE_THRESHOLD_HIGH:
        return MOUSE_STEP_HIGH
    elif axis_steps > MOUSE_THRESHOLD_MEDIUM:
        return MOUSE_STEP_MEDIUM
    elif axis_steps > MOUSE_THRESHOLD_LOW:
        return MOUSE_STEP_LOW
    elif axis_steps < -MOUSE_THRESHOLD_HIGH:
        return -MOUSE_STEP_HIGH
    elif axis_steps < -MOUSE_THRESHOLD_MEDIUM:
        return -MOUSE_STEP_MEDIUM
    elif axis_steps < -MOUSE_THRESHOLD_LOW:
        return -MOUSE_STEP_LOW
    return 0

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

# Combined main loop
while True:
    # Mouse control
    x = get_voltage(x_axis)
    y = get_voltage(y_axis)

    if not select.value:
        mouse.click(Mouse.RIGHT_BUTTON)
        time.sleep(0.2)  # Debounce delay

    x_steps = steps(x - (POT_MAX / 2))
    y_steps = steps(y - (POT_MAX / 2))

    x_move = calculate_movement(x_steps)
    y_move = calculate_movement(y_steps)  # Invert y value for standard orientation

    mouse.move(x=x_move, y=y_move)
    
    # Keyboard control
    scankeys()
    
    time.sleep(0.01)  # Add a short delay to manage the loop timing
