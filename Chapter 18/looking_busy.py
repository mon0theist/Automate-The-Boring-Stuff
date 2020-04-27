#! /usr/bin/python
#
# ATBS - Chapter 18 - Looking Busy

import pyautogui, time

print('You are now Looking Busy. Press CTRL+C to cancel')
try:
    while True:
        time.sleep(10)
        pyautogui.moveRel((1, 1))
        print('Sanity Check: mouse has been moved to ' + str(pyautogui.position()))
except KeyboardInterrupt:
    print('Program ended by user (CTRL+C)')
