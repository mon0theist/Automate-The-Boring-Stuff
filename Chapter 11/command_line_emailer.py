#! /usr/bin/python
#
# ATBS Chapter 11 - Practice Projects - Command Line Emailer
#
# Write a program that takes an email address and string of text on the command line and then, using Selenium, logs into your email account and sends an email of the string to the provided address. (You might want to set up a separate email account for this program.)
#
# This would be a nice way to add a notification feature to your programs. You could also write a similar program to send messages from a Facebook or Twitter account.

from selenium import webdriver
import sys, bs4, webbrowser

# TODO:
# Determine email address and string with sys.argv (recipient and string variables?)
# sys.argv[0] is command itself, sys.argv[1] is email address, sys.argv[2] is string

# open whatever webmail service (gmail/yahoo/whatever) with webbrowser
# use Selenium to figure out where the login prompt is
# use Selenium to sign in to webmail service
# use Selenium to Compose new email
# use Selenium to enter To: field
# use Selenium to paste/print string into body of email
# use Selenium to click Send
