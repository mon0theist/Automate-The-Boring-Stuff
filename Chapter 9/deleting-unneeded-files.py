#! /usr/bin/python3
# ATBS Chapter 9 Practice Projects

# Deleting Unneeded Files

# It’s not uncommon for a few unneeded but humongous files or folders to take up
# the bulk of the space on your hard drive. If you’re trying to free up room on
# your computer, you’ll get the most bang for your buck by deleting the most
# massive of the unwanted files. But first you have to find them.

# Write a program that walks through a folder tree and searches for exceptionally
# large files or folders—say, ones that have a file size of more than 100MB.
# (Remember, to get a file’s size, you can use os.path.getsize() from the os
# module.) Print these files with their absolute path to the screen.

# import modules
import os, re, shutil

# determine working directory
while True:
    print('The current directory is: ' + os.getcwd())
    dir_check = input('Do you want to change directory? [y/n] ').lower()
    if dir_check == 'y':
        newdir = os.path.abspath(input('Please enter full path to new directory: \n'))
        if os.path.exists(newdir) and os.path.isdir(newdir):
            os.chdir(newdir)
            walk_dir = newdir
            break
        else:
            print('Invalid path, try again\n')
    elif dir_check == 'n':
        walk_dir = os.getcwd()
        break
    else:
        print('Invalid entry\n')

print('The current directory is now: ' + os.getcwd())

print('Searching for files 100MB and larger...')

# os.walk() on working directory
for foldername, subfolders, filenames in os.walk(walk_dir):
    for files in filenames:
        if os.path.getsize(files) >= 100000000:
            print(os.path.abspath(files) + ' is ' + (str(os.path.getsize(files) / 1000000)) + ' MB')

# if os.path.getsize() >= 100MB, print file
