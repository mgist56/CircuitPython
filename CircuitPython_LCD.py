# Meg Gist
# CircuitPython LCD
# Thanks Seanan
# Again

# https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython/buttons-and-switch
# https://learn.adafruit.com/i2c-spi-lcd-backpack/python-circuitpython
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
import time
import board
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)
# I2c adresses at 0X27 or 0X3F
# Our LCDs are 2X16

buttonCounter = 0
switchCounter = True

button = digitalio.DigitalInOut(board.D0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

switch = digitalio.DigitalInOut(board.D2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

while True:
    if switch.value:
        switchCounter = True
        if button.value:
            buttonCounter += 1
            print(buttonCounter)
            print(switchCounter)
    else:
        switchCounter = False
        if button.value:
            buttonCounter -= 1
            print(buttonCounter)
            print(switchCounter)
    lcd.set_cursor_pos(1, 0)
    lcd.print("Presses:")
    lcd.print(str(buttonCounter))
    lcd.print("       ")
    lcd.set_cursor_pos(0, 0)
    # Setting the cursor to the top left
    lcd.print("Switch:")
    lcd.print(str(switchCounter))
    lcd.print(" ")