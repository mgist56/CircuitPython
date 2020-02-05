# Meg Gist
# CircuitPython Photointerrupters

import time
import board
import digitalio

# interruptValue is a variable for photo.value
# if InterruptValue = True, photointerrupter is interrupted
interruptValue = False
interruptCounter = 0
# time.monotonic() is just measuring time as it increases
initial = time.monotonic()

# setting up the photointerrupter
photo = digitalio.DigitalInOut(board.D2)
photo.direction = digitalio.Direction.INPUT
photo.pull = digitalio.Pull.UP

while True:
    now = time.monotonic()
    # and 3 milliseconds passes
    if now > initial + 4:
        print("The number of interrupts is:", interruptCounter)
        # reseting time to the time immediately after code runs
        initial = now
    # photo.value is true when photointerrupter is interrupted
    # if photointerrupter is continuously interrupted, it reads true continuously
    # "and not interruptValue" stops counter from increasing exponentially
    # and from crashing my computer as I think I did on a few occasions
    if photo.value and not interruptValue:
        interruptCounter = interruptCounter + 1
    # interruptValue begins as False initially
    # and resets to False after photointerrupter stops being interrupted
    # since both are true, "interruptCounter = interruptCounter + 1" only works once
    interruptValue = photo.value
