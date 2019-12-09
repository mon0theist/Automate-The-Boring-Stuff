#! /usr/bin/python3
# ATBS Chapter 7 Practice Project
# Strong Password Detection

# Write a function that uses regular expressions to make sure the password
# string it is passed is strong.

# A strong password has:
# at least 8 chars - .{8,}
# both uppercase and lowercase chars - [a-zA-Z]
#   test that BOTH exist, not just simply re.IGNORECASE
# at least one digit - \d+

# You may need to test the string against multiple regex patterns to validate its strength.

# NOTES
# Order shouldn't matter, & operator?
# Test: if regex search/findall != None
# seperate Regex for reach requirement?

import re

def pwStrength(pw):
    if eightChars.search(pw) and oneUpper.search(pw) and oneLower.search(pw) and oneDigit.search(pw) != None:
        print('Your password meets the requirements.')
    else:
        print('Your password does not meet the requirements.')

eightChars = re.compile(r'.{8,}') # tests for 8 or more chars
oneUpper = re.compile(r'[A-Z]+') # test for 1+ upper
oneLower = re.compile(r'[a-z]+') # test for 1+ lower
oneDigit = re.compile(r'\d+') # test for 1+ digit
# Wanted to combine all into single Regex if possible but can't figure it out

password = input('Please enter the password you want to test: ')
pwStrength(password)
