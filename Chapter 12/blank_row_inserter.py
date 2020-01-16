#! /usr/bin/python
#
# ATBS Chapter 12 - Practice Projects - Blank Row Inserter
#
# Create a program that takes two integers and a filename string as command line
# arguments. Let’s call the first integer N and the second integer M. Starting at
# row N, the program should insert M blank rows into the spreadsheet. For example,
# when the program is run like this:
#
# python blankRowInserter.py 3 2 myProduce.xlsx
#
# the “before” and “after” spreadsheets should look like Figure 12-12.
#
# You can write this program by reading in the contents of the spreadsheet. Then,
# when writing out the new spreadsheet, use a for loop to copy the first N lines.
# For the remaining lines, add M to the row number in the output spreadsheet.

import openpyxl, sys, os
