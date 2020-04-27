#! /usr/bin/python
#
# ATBS - Chapter 18 - mouse_now.py
# Displays the mouse cursor's current position

import pyautogui
print('Press CTRL+C to quit')
# Get and print the mouse coordinates
try:
    while True:
        # Get and print the mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
