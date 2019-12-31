#! /usr/bin/python
#
# ATBS Chapter 11 - Practice Projects - Command Line Emailer
#
# Write a program that takes an email address and string of text on the command
# line and then, using Selenium, logs into your email account and sends an email
# of the string to the provided address. (You might want to set up a separate
# email account for this program.)
#
# This would be a nice way to add a notification feature to your programs.
# You could also write a similar program to send messages from a Facebook or Twitter account.
#
# Selenim documentation:
# https://selenium-python.readthedocs.io/locating-elements.html
#
# Usage (from Linux):
# python command_line_emailer.py [email address] [text string in quotes]

from selenium import webdriver
import sys, bs4, webbrowser, time

# Try/Except structure in case of errors
try:
    # Get recipient email address and text string
    email = str(sys.argv[1])
    string = str(sys.argv[2])

    # open Yahoo Mail
    browser = webdriver.Firefox()
    browser.get('https://mail.yahoo.com')
    time.sleep(5) # 5 second sleep, give page time to load

    # Selenim already opens Firefox with a clean profile:
    # https://stackoverflow.com/questions/27630190/python-selenium-incognito-private-mode

    # Click the Sign In button
    sign_in = browser.find_element_by_link_text('Sign in')
    sign_in.click()
    time.sleep(5) # 5 second sleep, give page time to load

    # use Selenium to figure out where the login prompt is
    username = browser.find_element_by_id('login-username')

    # use Selenium to sign in to webmail service
    username.send_keys('pythonic.chronic@yahoo.com')
    next = browser.find_element_by_id('login-signin')
    next.click() # could also do username.send_keys(Keys.ENTER) but may be less accurate
    time.sleep(5) # 5 second sleep, give page time to load

    passwd = browser.find_element_by_id('login-passwd')
    passwd.send_keys('insert_password')
    next = browser.find_element_by_id('login-signin') # this has to be repeated otherwise it will give a "stale" error
    next.click()
    time.sleep(5) # 5 second sleep, give page time to load

    # Compose new email
    compose = browser.find_element_by_link_text('Compose')
    compose.click()

    # To
    recipient = browser.find_element_by_id('message-to-field')
    recipient.send_keys(email)

    # had to use find_element_by_xpath() for the rest of these, nothing else would work

    # Subject
    subject = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div/input")
    subject.click()
    subject.send_keys('Email from Python (command_line_emailer.py)')

    # Body
    body = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[1]")
    body.click()
    body.send_keys(string)

    # Send
    send = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/button")
    send.click()

    # close Firefox
    time.sleep(5)
    browser.quit()

except Exception as exc:
    print("There was an exception: %s" % (exc))
    sys.exit() # exits program in case of error
