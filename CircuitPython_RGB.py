# Meg Gist
# RGB
# Thanks, Imogen
# https://tinyurl.com/commonanodeRGBLED
# https://www.w3schools.com/colors/colors_picker.asp

import pulseio
# we need pulseio; metro only has one analog
import time
maxVal = 65531
# also 2**16-1
class RGB:
    kind = "color"  # class variable shared by all instances
    # don't need __init__ method, but common for running instantiaion

    def __init__(self, r, g, b):
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)

    def change_name(self, newName):
        self.name = newName
    # max duty_cycle turns color off
    # min duty_cycle turns color on
    # duty_cycle is basically value

    def red(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = maxVal
        self.pwm_b.duty_cycle = maxVal

    def green(self):
        self.pwm_r.duty_cycle = maxVal
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = maxVal

    def blue(self):
        self.pwm_r.duty_cycle = maxVal
        self.pwm_g.duty_cycle = maxVal
        self.pwm_b.duty_cycle = 0

    def cyan(self):
        self.pwm_r.duty_cycle = maxVal
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 0

    def magenta(self):
        # isn't this purple tho
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = maxVal
        self.pwm_b.duty_cycle = 0

    def yellow(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = maxVal

    def rainbow(self):
        #  works by slowly fading r, g, and b simultaniously
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = maxVal
        self.pwm_b.duty_cycle = maxVal
        for val in range(0,2**16,64):
            #red
            self.pwm_r.duty_cycle = val
            self.pwm_g.duty_cycle = maxVal-val
            self.pwm_b.duty_cycle = maxVal
            time.sleep(.01)
        for val in range(0,2**16,64):
            #green
            self.pwm_r.duty_cycle = maxVal
            self.pwm_g.duty_cycle = val
            self.pwm_b.duty_cycle = maxVal-val
            time.sleep(.01)
        for val in range(0,2**16,64):
            #blue
            self.pwm_r.duty_cycle = maxVal-val
            self.pwm_g.duty_cycle = maxVal
            self.pwm_b.duty_cycle = val
            time.sleep(.01)