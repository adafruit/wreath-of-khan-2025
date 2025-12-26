import displayio

from adafruit_qualia.graphics import Displays, Graphics

# For other displays:
# 2.1" Round = Displays.ROUND21
# 3.4" Square = Displays.SQUARE34
graphics = Graphics(Displays.ROUND40, default_bg="/khan.bmp", auto_refresh=False)

graphics.display.auto_refresh = True

while True:
    pass