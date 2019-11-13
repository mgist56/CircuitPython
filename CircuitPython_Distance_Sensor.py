# Meg Gist
# CircuitPython Distance Sensor
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio
radishBat = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
# "radishBat" being the distance sensor
candyCorn = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)
# "candyCorn" being the NeoPixel
r = 0
b = 0
g = 0
# [0, ... , 20]
# [255, ... , 0]
while True:
# So turns out it's literally a function
    try:
        dist = radishBat.distance
        # The color of the NeoPixel changes depending on the distance of the sensor
        if dist <= 20:
            # Syntax (using domain and range in respect to treating like a function):
            # map_range(x(in this case, distance), domain min, domain max, range min, range max)
            r = simpleio.map_range(dist, 0, 20, 255, 0)
            b = simpleio.map_range(dist, 5, 20, 0, 255)
            g = simpleio.map_range(dist, 20, 35, 0, 255)
        else:
            r = simpleio.map_range(dist, 0, 20, 255, 0)
            b = simpleio.map_range(dist, 20, 35, 255, 0)
            g = simpleio.map_range(dist, 20, 35, 0, 255)
        candyCorn.fill((int(r), int(g), int(b)))
    except RuntimeError:
        # If there's an error print "boop" instead of attempting to change color
        print("boop")
        time.sleep(0.1)
