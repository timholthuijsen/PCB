import board
import digitalio
import time
import pwmio
#ledpin = digitalio.DigitalInOut(board.GP20)
#ledpin.direction = digitalio.Direction.OUTPUT
#ledpin.value = True




#Set up PWM on GP21
led = pwmio.PWMOut(board.GP21, frequency=5000, duty_cycle=0)

#Function to set LED brightness
def set_brightness(brightness):
    # Brightness should be a value between 0 (off) and 65535 (full brightness)
    led.duty_cycle = brightness

set_brightness(200)

time.sleep(2)

set_brightness(6500)

time.sleep(1)

led.deinit()