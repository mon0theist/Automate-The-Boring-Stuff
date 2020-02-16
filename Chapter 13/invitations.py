#! /usr/bin/python
#
# Automate the Boring Stuff - Chapter 13 - Custom Invitations as Word Documents
#
# Say you have a text file of guest names. This guests.txt file has one name per line, as follows:
#
# Prof. Plum
# Miss Scarlet
# Col. Mustard
# Al Sweigart
# Robocop
#
# Write a program that would generate a Word document with custom invitations that look like Figure 13-11.
#
# Since Python-Docx can use only those styles that already exist in the Word
# document, you will have to first add these styles to a blank Word file and then
# open that file with Python-Docx. There should be one invitation per page in the
# resulting Word document, so call add_break() to add a page break after the last
# paragraph of each invitation. This way, you will need to open only one Word
# document to print all of the invitations at once.
#
# fomat of Word doc:
# Brush Script Std
# Times New Roman bold center
# Brush Script Std

## SKIPPING This
# I don't know how to create Styles in LibreOffice Writer and it's too much of a pain
# to figure out

import docx

gfile = open('guests.txt', 'r')
glist = gfile.readlines()
# need to figure out how to get rid of \n's from readlines()
# maybe regex? Oh God no...

# create blank doc with styles
blankdoc = docx.Document('blank.docx')

# TODO:
# Create Doc file
doc = docx.Document('invitation.docx')
#   Set styles for runs
#   create runs
#   set styles again if needed
