from adafruit_circuitplayground.bluefruit import cpb

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


cpb.pixels.auto_write = True
kbd = Keyboard(usb_hid.devices)

mute = False
 
def toggle_state():
  global mute

  mute = not mute
  for i in range(10):
    if mute:
      cpb.pixels[i] = (255, 0, 0)
    else:
      cpb.pixels[i] = (0, 255, 0)  

toggle_state()
while True:
  if cpb.button_a | cpb.button_b:
    kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)  # SHIFT-CONTROL-M (Teams Mute)
    toggle_state()

    while cpb.button_a | cpb.button_b: # Wait for button to be released
      pass
