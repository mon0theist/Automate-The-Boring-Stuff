#! /usr/bin/python
#
# ATBS Chapter 11 - Practice Projects - Command Line Emailer
#
# Write a program that takes an email address and string of text on the command line and then, using Selenium, logs into your email account and sends an email of the string to the provided address. (You might want to set up a separate email account for this program.)
#
# This would be a nice way to add a notification feature to your programs. You could also write a similar program to send messages from a Facebook or Twitter account.

from selenium import webdriver
import sys, bs4, webbrowser, time
from selenium.webdriver.common.keys import Keys

# TODO:
# Determine email address and string with sys.argv (recipient and string variables?)
# sys.argv[0] is command itself, sys.argv[1] is email address, sys.argv[2] is string
# not sure if "python" will be included in sys.argv...

# Testing
# email = str(sys.argv[1])
email = 'bburns91@gmail.com'
# string = str(sys.argv[2])
string = 'Sup faggot'

# open whatever webmail service (gmail/yahoo/whatever) with selenium webdriver
browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')
time.sleep(5) # 5 second sleep, give page time to load

# browser will likely auto-login, as both Chrome and Firefox are logged in with my
# Google account. Will need to open in Incognito/Private Browsing.
# Firefox is CTRL+SHIFT+P
#
# Actually it seems Selenim already opens Firefox with a clean profile anyway:
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
next.click()
# could also do username.send_keys(Keys.ENTER) but may be less accurate
time.sleep(5) # 5 second sleep, give page time to load

passwd = browser.find_element_by_id('login-passwd')
passwd.send_keys('4EAw6QK9cErecG9w')
next = browser.find_element_by_id('login-signin') # this has to be repeated otherwise it will give a "stale" error
next.click()
time.sleep(5) # 5 second sleep, give page time to load

# use Selenium to Compose new email
compose = browser.find_element_by_link_text('Compose')
compose.click()

# use Selenium to enter To: field
recipient = browser.find_element_by_id('message-to-field')
recipient.click() # probably not necessary but trying to ensure accuracy
recipient.send_keys(email)
time.sleep(1)

subject = browser.find_element_by_id('q_T y_Z2uhb3X je_0 jb_0 X_0 N_fq7 G_e A_6EqO C_Z281SGl ir_0 P_0 bj3_Z281SGl b_0 j_n d_72FG em_N')
subject.click()
print('Email from Python (command_line_emailer.py)')
time.sleep(1)

# recipient.send_keys(Keys.TAB)
# time.sleep(1)
# recipient.send_keys(Keys.TAB)
# time.sleep(1)
# recipient.send_keys(Keys.TAB) # Subject takes 3 Tabs to work

#recipient.send_keys(Keys.TAB) # Body
body = browser.find_element_by_id('rte em_N ir_0 iy_A iz_h N_6Fd5')
body.click()
time.sleep(1)
# use Selenium to paste/print string into body of email
recipient.send_keys(string) # paste string, body of email

# use Selenium to click Send
send = browser.find_element_by_link_text('Send')
