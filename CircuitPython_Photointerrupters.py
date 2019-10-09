# Meg Gist
# CircuitPython Photointerrupters

import time
import board
import digitalio

interruptValue = False
interruptCounter = 0
initial = time.monotonic()

photo = digitalio.DigitalInOut(board.D2)
photo.direction = digitalio.Direction.INPUT
photo.pull = digitalio.Pull.UP

while True:
    now = time.monotonic()
    if now > initial + 4:
        # and 3 milliseconds passes
        print("The number of interrupts is:", interruptCounter)
        initial = now
    if photo.value and not interruptValue:
        interruptCounter = interruptCounter + 1
    interruptValue = photo.value