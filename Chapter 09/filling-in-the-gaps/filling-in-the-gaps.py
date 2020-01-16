#! /usr/bin/python3
# ATBS Chapter 9 Practice Projects

# Filling in the Gaps

# Write a program that finds all files with a given prefix, such as spam001.txt,
# spam002.txt, and so on, in a single folder and locates any gaps in the
# numbering (such as if there is a spam001.txt and spam003.txt but no
# spam002.txt). Have the program rename all the later files to close this gap.

# As an added challenge, write another program that can insert gaps into
# numbered files so that a new file can be added.

# **** THIS DOES NOT WORK ****
# Might revisit and fix later but I want to move on and finish this book


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
print("File prefix is 'spam###.txt' ")

# counters
i = 1
# n = 0

file_pattern_regex = re.compile(r"""
(spam)
(\d\d\d)
(\.txt)
""", re.VERBOSE)

# os.walk() on working directory
for foldername, subfolders, filenames in os.walk(walk_dir):
    for file in filenames:
        mo = file_pattern_regex.search(file)
        if mo.group(2) == ('00' + str(i)):
            i = i + 1
            print('i is currently ' + str(i)) # testing
            continue
        elif mo.group(2) != i:
            # contruct new string with string concatenation, mo.group(), shutil.move()
            # filename_str = str(file) - don't think this is needed
            if i < 10:
                new_file = 'spam' + '00' + str(i) + '.txt'
                print('Renaming ' + file + ' to ' + new_file)
                shutil.move(file, new_file)
            elif i >= 11 and i < 100:
                new_file = 'spam' + '0' + str(i) + '.txt'
                print('Renaming ' + file + ' to ' + new_file)
                shutil.move(file, new_file)
            elif i >= 100:
                new_file = 'spam' + str(i) + '.txt'
                print('Renaming ' + file + ' to ' + new_file)
                shutil.move(file, new_file)
            i = i + 1
            print('i is currently ' + str(i)) # testing
