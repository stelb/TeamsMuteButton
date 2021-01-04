import board
import neopixel

from adafruit_circuitplayground.bluefruit import cpb

import adafruit_fancyled.adafruit_fancyled as fancy

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
 
while True:
    if cpb.button_a | cpb.button_b:
        kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)  # SHIFT-CONTROL-M (Teams Mute)
        while cpb.button_a | cpb.button_b: # Wait for button to be released
            pass
