#! /usr/bin/python
#
# ATBS Chapter 11 - Practice Projects - 2048
#
# 2048 is a simple game where you combine tiles by sliding them up, down, left,
# or right with the arrow keys. You can actually get a fairly high score by
# repeatedly sliding in an up, right, down, and left pattern over and over again.
# Write a program that will open the game at https://gabrielecirulli.github.io/2048/
# and keep sending up, right, down, and left keystrokes to automatically play the game.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

print()
print('If you get a game over, click "Try Again" to automatically play another game.')
print()
print('To terminate program, hit CTRL+C on the terminal, or simply close the Firefox window.')
print()

try:
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')

    moveslist = [
    Keys.UP,
    Keys.DOWN,
    Keys.LEFT,
    Keys.RIGHT
    ]

    html = browser.find_element_by_tag_name('html')

    while True:
        html.send_keys(random.choice(moveslist))
        # would like to be able to detect a Game Over but not sure how
        # While searching for this <gameoverbutton> element returns an error:
        #   keep playing
except Exception:
    print('Firefox has been closed')
except KeyboardInterrupt:
    print('\nCTRL+C was entered at the terminal.')
