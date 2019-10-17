# https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
import digitalio
import random
import time

Q = True
P = False

class FancyLED:
    kind = "pattern"

    def __init__(self, pin1, pin2, pin3):
        self.led1 = digitalio.DigitalInOut(pin1)
        self.led1.direction = digitalio.Direction.OUTPUT
        self.led2 = digitalio.DigitalInOut(pin2)
        self.led2.direction = digitalio.Direction.OUTPUT
        self.led3 = digitalio.DigitalInOut(pin3)
        self.led3.direction = digitalio.Direction.OUTPUT

    def alternate(self):
        print("alternate")
        self.led1.value = Q
        self.led2.value = P
        self.led3.value = Q
        time.sleep(0.5)
        self.led1.value = P
        self.led2.value = Q
        self.led3.value = P
        time.sleep(0.5)
        self.led1.value = Q
        self.led2.value = P
        self.led3.value = Q
        time.sleep(0.5)
        # Turning off all LEDS
        self.led1.value = P
        self.led2.value = P
        self.led3.value = P
        time.sleep(0.5)

    def blink(self):
        print("blink")
        self.led1.value = Q
        self.led2.value = Q
        self.led3.value = Q
        time.sleep(0.5)
        self.led1.value = P
        self.led2.value = P
        self.led3.value = P
        time.sleep(0.5)
        self.led1.value = Q
        self.led2.value = Q
        self.led3.value = Q
        time.sleep(0.5)
        # Turning off all LEDS
        self.led1.value = P
        self.led2.value = P
        self.led3.value = P
        time.sleep(0.5)

    def chase(self):
        print("chase")
        self.led1.value = Q
        self.led2.value = P
        self.led3.value = P
        time.sleep(0.5)
        self.led1.value = P
        self.led2.value = Q
        self.led3.value = P
        time.sleep(0.5)
        self.led1.value = P
        self.led2.value = P
        self.led3.value = Q
        time.sleep(0.5)
        self.led1.value = P
        self.led2.value = Q
        self.led3.value = P
        time.sleep(0.5)
        self.led1.value = Q
        self.led2.value = P
        self.led3.value = P
        time.sleep(0.5)
        # Turning off all LEDS
        self.led1.value = P
        self.led2.value = P
        self.led3.value = P
        time.sleep(0.5)

    def sparkle(self):
        for whatever in range(0, 50):
        # Turns on the random LED 50 times
        # Creates the "sparkle" effect
            print("sparkle")
            H = random.randint(1, 3)
            # Picks random LED 1-3
            # "H" a placeholder value
            if H == 1:
                self.led1.value = Q
                # Calling this LED "1"
                self.led2.value = P
                self.led3.value = P

            elif H == 2:
                self.led1.value = P
                self.led2.value = Q
                # Calling this LED "2"
                self.led3.value = P

            elif H == 3:
                self.led1.value = P
                self.led2.value = P
                self.led3.value = Q
                # Calling this LED "3"
            time.sleep(.05)
            # Turning off all LEDS
            self.led1.value = P
            self.led2.value = P
            self.led3.value = P