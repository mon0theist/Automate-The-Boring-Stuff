#! /usr/bin/python3
# ATBS Chapter 9 Practice Projects

# Selective Copy

# Write a program that walks through a folder tree and searches for files with a
# certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder.

# import required modules
import os, shutil, re, pprint

# create regexes for different file extensions (jpg, pdf, doc, txt, etc...)
# regex pattern should be:
# (anything at the beginning)(.)(file extension at the end)

jpg_regex = re.compile(r'^(.*?)(\.)(jpg|jpeg)$', re.IGNORECASE)

pdf_regex = re.compile(r'^(.*?)(\.)(pdf)$', re.IGNORECASE)

doc_regex = re.compile(r'^(.*?)(\.)(doc|docx)$', re.IGNORECASE) # include docx

txt_regex = re.compile(r'^(.*?)(\.)(txt)$', re.IGNORECASE)

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


# determine file extension, use corresponding regex
while True:
    filetype = input('What filetype to search? [jpg/pdf/doc/txt] \n').lower()
    if filetype == 'jpg':
        regex = jpg_regex
        break
    elif filetype == 'pdf':
        regex = pdf_regex
        break
    elif filetype == 'doc':
        regex = doc_regex
        break
    elif filetype == 'txt':
        regex = txt_regex
        break
    else:
        print('Invalid selection, please try again\n')

# determine destination directory
while True:
    dest_dir = os.path.abspath(input('Please enter destination folder (full path):\n'))
    if os.path.exists(dest_dir) and os.path.isdir(dest_dir):
        break
    else:
        print('Invalid path, try again\n')

# os.walk() through working directory, searching with regex
for foldername, subfolders, filename in os.walk(walk_dir):
    for files in filename:
        # print(files)
        mo = regex.search(files)
        if not mo == None:
            shutil.copy(os.path.join(os.getcwd(), files), os.path.join(dest_dir, files))
            print(files + ' has been copied to destination...')
