# CircuitPython
Meg CircuitPython

https://github.com/chssigma/Markdown_Cheatsheet

http://wiki.chssigma.com/index.php?title=User:Mgist56

## Hello CircuitPython
First CircuitPython assignment; making an LED fade in and out.
### Resources
https://learn.adafruit.com/series/adafruit-io-basics
### Wiring
<img src="Media/HelloCircuitPython.jpg" width="300">

### Takeaways
CircuitPython coding is weird. "While True:" is basically the same thing as "void loop(){}" and for “time.sleep(secs)” (which is the Python equivalent of Arduino’s “delay(ms)”) you need to import time at the top of your code. I used an 
elif statement to change the way the LED was fading (brightening or dimming).

## CircuitPython Servo
Second CircuitPython assignment; servo direction using capacitive touch.
### Resources
https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython/capacitive-touch

https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/circuitpython-servo
### Wiring
<img src="Media/CircuitPythonServo.jpg" width="300">

### Takeaways
Capacitive touch/cap touch uses touchio. “if not touch_A0.value and not touch_A4.value:” stopped the servo from doing anything weird when neither of the wires were being touched. It must be an if statement and not an else statement because an else statement would have canceled out the previous if statements.

## CircuitPython LCD
Third CircuitPython assignment; button/switch counter on LCD.
### Resources
https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython/buttons-and-switch

https://learn.adafruit.com/i2c-spi-lcd-backpack/python-circuitpython

https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
### Wiring
<img src="Media/CircuitPythonLCD.jpg" width="300">

### Takeaways
Pulling up means setting an input voltage as high. Using a string in “lcd.print(str(buttonCounter))” instead of just “lcd.print(buttonCounter)” makes sure that the LCD prints out the buttonCounter’s actual numerical value instead of the variable “buttonCounter.” Oh, and “lcd.print("       ")” prevents any strange mishaps in which the LCD would print the value of the buttonCounter on top of/replacing the letters from “lcd.print("Presses:")” (the number of spaces should correspond to the number of characters in the line being printed).

## CircuitPython Photointerrupters
Fourth CircuitPython Assignment; photointerrupter interrupt counter.
### Resources
### Wiring
<img src="Media/CircuitPythonPhotointerrupters.jpg" width="300">

### Takeaways
“time.monotonic()” simply measures the time passing (which in this case was in milliseconds). “if photo.value and not interruptValue:” is **extremely** important because it prevents the interruptCounter from increasing exponentially and crashing Mu. It works like this: interruptValue is False at the beginning. When the photointerrupter is first interrupted, photo.value becomes True, but interruptValue is still false, since it is not the same as photo.value until after that if statement. Because of that, the counter increases once, at which point the interruptValue then becomes equal to photo.value and stops the counter from counting.

## CircuitPython Distance Sensor
Fifth CircuitPython assignment; NeoPixel color change with HCSRO4 sensor.
### Resources
### Wiring
<img src="Media/HelloCircuitPython.jpg" width="300">

### Takeaways
“simplio.map_range()” is pretty much setting the parameters for each value r, g, and b, as parameters like a math function. Everything is just broken down to the individual axis parameter level. The x and y values of r, g, and b, are set in order to determine a point that increases or decreases depending on the data from the distance sensor, at which point the neopixel changes colors with those three values.

## CircuitPython RGB
Sixth CircuitPython assignment; common anode RGB LED color change with RGB library.
### Resources
https://www.hackster.io/techmirtz/using-common-cathode-and-common-anode-rgb-led-with-arduino-7f3aa9
### Wiring
<img src="Media/CircuitPythonRGB.jpg" width="300">

### Takeaways
Since the Metro only has one analog, pulseio is needed instead when making the RGB class. When determining the color values for the LEDs, three things are important: max duty_cycle turns the color off, min duty_cycle turns the color on, and duty_cycle is basically value but in Python code. “maxVal = 65531” just sets a variable for a number, which in this case is the highest value that the common anode RGB LEDs are capable of emitting.

## Hello VS Code
### Resources
### Wiring
N/A
### Takeaways
VS code is really useful and time saving. Also, mousing over is important and is **not** the same thing as clicking on something. You can stage multiple untracked files by mousing over them and clicking “+.”

## CircuitPython Fancy LED
Eighth CircuitPython assignment; six LED patterns using four custom methods.
### Resources
### Wiring
<img src="Media/CircuitPythonFancyLED.jpg" width="300">

### Takeaways
If you can recycle old code, do so. This assignment is pretty much the exact same thing as the CircuitPython RGB assignment but with six LEDs instead of two common anode RGB LEDs. I found it especially useful to use variables when setting the values for each self.led.value because it saved me from typing out the words “true” and “false” an excessive amount of times. However, note to self: use variables that make sense instead of just random letters that you will probably forget the assigned values to. “T” and “F” will do just fine next time.

## Assignment Template

### Resources

### Wiring

### Takeaways
