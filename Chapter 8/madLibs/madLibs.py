#! /usr/bin/python
# ATBS Chapter 8 Practice Projects - Mad Libs
#
# Create a Mad Libs program that reads in text files and lets the user add their
# own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text
# file. For example, a text file may look like this:
#
# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
# unaffected by these events.
# The results should be printed to the screen and saved to a new text file.


# Open the madlib file
madlibFile = open('madlibs.txt')

# Read contents of file, save as a string to a variable
template = madlibFile.read()

# Prompt user for ADJ, NOUN, ADVERB, and VERB values
adj = input('Please enter an adjective:\n')
noun = input('Please enter a noun:\n')
noun2 = input('Please enter another noun:\n')
adv = input('Please enter an adverb:\n')
verb = input('Please enter a verb (past tense):\n')

# replace template words with user inputs - 'str'.replace() method
template = template.replace('ADJECTIVE', adj)
template = template.replace('NOUN', noun, 1)
template = template.replace('NOUN', noun2, 2)
template = template.replace('ADVERB', adv)
template = template.replace('VERB', verb)

# Write results to new text file, and print results to screen
print(template)
madlibResults = open('results.txt', 'w')
madlibResults.write(template)

# close the file(s)
madlibFile.close()
madlibResults.close()
