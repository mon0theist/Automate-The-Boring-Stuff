#! /usr/bin/python3
# ATBS Chapter 8: mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: <python> mcb.pyw save <keyword> - Saves clipboard to keyword.
#        <python> mcb.pyw <keyword> - Loads keyword to clipboard.
#        <python> mcb.pyw list - Loads all keywords to clipboard.

# Chapter 8 Practice Project: Extending the Multiclipboard
# Extend the multiclipboard program in this chapter so that it has a delete
# <keyword> command line argument that will delete a keyword from the shelf.
# Then add a delete command line argument that will delete all keywords.

# Usage: <python> mcb.pyw delete <keyword> - Deletes keyword from clip
#        <python> mcb.pyw delete - Deletes all keywords

import pyperclip, sys, shelve, pprint

mcbShelf = shelve.open('mcb')
# shelve functions similarly to a dict, so you can call values of the shelve
# by shelve[key]

# Add a new keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print("The new keyword \'" + str(sys.argv[2]) + "\' has been saved.")
# Delete a keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    print('Keyword \'' + str(sys.argv[2]) + '\' has been deleted')
    del mcbShelf[sys.argv[2]]
# if only 1 arg:
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('Current keywords (copied to clipboard):')
        pprint.pprint(list(mcbShelf.keys()))
    # delete all keywords
    elif sys.argv[1].lower() == 'delete':
        answer = input('Are you sure you want to delete all keywords? (y/n) ')
        if answer.lower() == 'y':
            mcbShelf.clear()
            print('All keywords have been deleted')
    # copy the clipboard value of the keyword
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
