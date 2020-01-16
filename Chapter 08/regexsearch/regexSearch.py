#! /usr/bin/python
# ATBS Chapter 8 Practice Project - Regex Search

# Write a program that opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression. The results should be printed
# to the screen.

# import required module(s)
import os, re

# confirm directory
while True:
    print('The current directory is: ' + os.getcwd())
    dir = input('Do you want to change directory? [y/n]').lower()
    if dir == 'y':
        newdir = input('Please enter full path to new directory: \n')
        if os.path.exists(newdir) and os.path.isdir(newdir):
            os.chdir(newdir)
            break
        else:
            print('Invalid path, try again\n')
    elif dir == 'n':
        break
    else:
        print('Invalid entry\n')

# testing
print('The current directory is now: ' + os.getcwd())

# prompt for user input for regex (input() with raw string?)
user_regex = re.compile(input('Please enter your regex (hint: phone number): \n'))

# open all text files in the working directory (requires loop?
# os.listdir(), os.path.join(), os.path.exists()?, .endswith()
#
# find/determine all .txt files in cwd
# open all .txt files in cwd
# perform regex search on opened file(s)
# maybe each iteration of loop does one file at a time??

file_list = os.listdir()
print()

for i in range(len(file_list)):
    if file_list[i].endswith('.txt') == True:
        open_file = open(file_list[i], 'r')
        file_contents = open_file.read()
        open_file.close()
        mo = user_regex.search(file_contents)
        if mo == None:
            print('Search results from ' + str(file_list[i]) + ':')
            print('No results found')
            print()
        else:
            print('Search results from ' + str(file_list[i]) + ':')
            print(mo.group())
            print()
