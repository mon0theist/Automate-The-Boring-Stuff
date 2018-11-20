#! /usr/bin/python3
# ATBS Chapter 7 Practice Project
# Regex Version of Strip()

# Write a function that takes a string and does the same thing as the strip()
# string method. If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the
# string. Otherwise, the characters specified in the second argument to the
# function will be removed from the string.

import re,sys

def regexStrip(string, char=''):
    string = str(string)
    char = str(char)
    if char == '':
        spaces_mo = spaceRegex.search(string)
        print(spaces_mo.group(2))
    else:
        charRegex = re.compile(r'(^%s*)(.+?)(%s*$)' % (char, char))
        char_mo = charRegex.search(string)
        print(char_mo.group(2))

# testing
# print('String being stripped: ' + sys.argv[1])
# if sys.argv[2] != None:
#    print('Character used to strip: ' + sys.argv[2])
# print('Len of sys.argv: ' + str(len(sys.argv)))

if len(sys.argv) < 2:
    print('Error: not enough arguments used')
    exit()
elif len(sys.argv) == 2:
    regexStrip(sys.argv[1], ' ')
elif len(sys.argv) > 3:
    print('Error: too many arguments used')
    exit()
else:
    regexStrip(str(sys.argv[1]), str(sys.argv[2]))
