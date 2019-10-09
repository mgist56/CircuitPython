# Meg Gist
# Hello CircuitPython

import analogio
# importing the Analog In
import board
import time

#pin.deinit()
#led.direction = analogio.Direction.OUTPUT

led = analogio.AnalogOut(board.A0)
# like "dot = neopixel.NeoPixel(board.NEOPIXEL, 1)"
# but instead with the LED
B = 65000
# inital LED brightness value
amount = 1000
ceiling = 50000
# highest value the LED can omit
floor = 20000
# lowest value the LED can omit

while True:
    led.value = B
    B -= amount
    time.sleep(.01)
    if B < floor:
        amount = -1000
    elif B > ceiling:
        amount = 1000
    time.sleep(.01)