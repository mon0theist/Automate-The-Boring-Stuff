#! /usr/bin/python
#
# # ATBS Chapter 11 - "Ideas for Similar Programs"
# Open your favorite local weather provider for your area

# using weatherunderground.com
# use webbrowser to open weatherunderground.com/weather/
# https://www.wunderground.com/weather/us/il/aurora

import webbrowser

country = input('Please enter country (2-chars, US for USA): ').lower()
state = input('Please enter state (2-chars, IL for Illinois): ').lower()
city = input('Please enter city (i.e. Aurora): ').lower()

webbrowser.open('http://wunderground.com/weather/' + country + '/' + state + '/' + city)
