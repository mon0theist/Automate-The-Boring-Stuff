#! /usr/bin/python
#
# ATBS - Chapter 18 - Looking Busy
#
# Many instant messaging programs determine whether you are idle, or away from
# your computer, by detecting a lack of mouse movement over some period of
# time; say, ten minutes. Maybe you’d like to sneak away from your desk for a
# while but don’t want others to see your instant messenger status go into idle
# mode. Write a script to nudge your mouse cursor slightly every ten seconds.
# The nudge should be small enough so that it won’t get in the way if you do
# happen to need to use your computer while the script is running.

import pyautogui, time

print('You are now Looking Busy. Press CTRL+C to cancel')
try:
    while True:
        time.sleep(10)
        pyautogui.moveRel((1, 1))
        print('Sanity Check: mouse has been moved to ' + str(pyautogui.position()))
except KeyboardInterrupt:
    print('Program ended by user (CTRL+C)')
