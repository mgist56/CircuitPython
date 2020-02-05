# Meg Gist
# Classes, Objects, and Modules
# Thanks, Imogen

import time
import board
from rgb import RGB
# importing the RGB class from rgb module

r1 = board.D3
g1 = board.D4
b1 = board.D5
r2 = board.D11
g2 = board.D12
b2 = board.D13
# pwm sometimes is weird
# RGB2 pins were working at the same time

myRGB1 = RGB(r1, g1, b1)
myRGB2 = RGB(r2, g2, b2)
# wiring up the LEDs

myRGB1.red()
myRGB2.green()
time.sleep(1)
myRGB1.blue()
myRGB2.cyan()
time.sleep(1)
myRGB1.magenta()
myRGB2.yellow()
time.sleep(1)
myRGB1.rainbow()
myRGB2.rainbow()
# took away the rates because science
time.sleep(1)