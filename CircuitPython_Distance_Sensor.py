import time
import board
import adafruit_hcsr04
import neopixel
import simpleio
radishBat = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
candyCorn = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)
r = 0
b = 0
g = 0
# [0, ... , 20]
# [255, ... , 0]
while True:
    try:
        dist = radishBat.distance
        if dist <= 20:
            # map_range(x, domain min, domain max, range min, range max)
            r = simpleio.map_range(dist, 0, 20, 255, 0)
            b = simpleio.map_range(dist, 5, 20, 0, 255)
            g = simpleio.map_range(dist, 20, 35, 0, 255)
        else:
            r = simpleio.map_range(dist, 0, 20, 255, 0)
            b = simpleio.map_range(dist, 20, 35, 255, 0)
            g = simpleio.map_range(dist, 20, 35, 0, 255)
        candyCorn.fill((int(r), int(g), int(b)))
    except RuntimeError:
        print("boop")
        time.sleep(0.1)