#! /usr/bin/python3
#
# ATBS Chapter 11 - MapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)

# Ideas for Similar Programs
# As long as you have a URL, the webbrowser module lets users cut out the step
# of opening the browser and directing themselves to a website.
# Other programs could use this functionality to do the following:
# - Open all links on a page in separate browser tabs.
# - Open the browser to the URL for your local weather.
# - Open several social network sites that you regularly check.
