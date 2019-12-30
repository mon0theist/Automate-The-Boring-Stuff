#! /usr/bin/python
#
# ATBS Chapter 11 - Selenium Example
#
# Websites in this Selenium section have since been updated and a lot of the code
# in this section doesn't work anymore

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
