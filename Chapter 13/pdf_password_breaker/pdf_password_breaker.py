#! /usr/bin/python
#
# Automate the Boring Stuff - Chapter 13 - Brute Force PDF Password Breaker
#
# Say you have an encrypted PDF that you have forgotten the password to, but you
# remember it was a single English word. Trying to guess your forgotten password
# is quite a boring task. Instead you can write a program that will decrypt the
# PDF by trying every possible English word until it finds one that works. This
# is called a brute-force password attack. Download the text file dictionary.txt
# from http://nostarch.com/automatestuff/. This dictionary file contains over
# 44,000 English words with one word per line.
#
# Using the file-reading skills you learned in Chapter 8, create a list of word
# strings by reading this file. Then loop over each word in this list, passing
# it to the decrypt() method. If this method returns the integer 0, the password
# was wrong and your program should continue to the next password. If decrypt()
# returns 1, then your program should break out of the loop and print the hacked
# password. You should try both the uppercase and lower-case form of each word.
# (On my laptop, going through all 88,000 uppercase and lowercase words from the
# dictionary file takes a couple of minutes. This is why you shouldn’t use a
# simple English word for your passwords.)

import PyPDF2

# load encrypted pdf
pdf_file = open('encrypted.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
print('Loaded encrypted.pdf...')
if pdf_reader.isEncrypted == True:
    print('Confirmed encryption')
elif pdf_reader.isEncrypted == False:
    print('Error: File is not encrypted, exiting program')
    exit()

# open/read dictionary.txt
# read dictionary.txt into a list without newlines
namelist = open('dictionary.txt', 'r').read().splitlines()

# loop over each item in namelist
print('Attempting bruteforce with dictionary.txt using all-upper and all-lower cases...')
for i in range(len(namelist)):
    if pdf_reader.decrypt(namelist[i]) == 0 and pdf_reader.decrypt(namelist[i].lower()) == 0:
        print('Returned 0: Password incorrect: ' + str(namelist[i]))
        continue
    elif pdf_reader.decrypt(namelist[i]) == 1 or pdf_reader.decrypt(namelist[i].lower()) == 1:
        print('Returned 1: Password correct!')
        print('Password: ' + str(namelist[i]))
        break

print('Script complete, closing program...')
