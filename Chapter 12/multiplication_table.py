#! /usr/bin/python
#
# ATBS Chapter 12 - Practice Projects - Multiplication Table Maker
#
# Create a program multiplicationTable.py that takes a number N from the command
# line and creates an N×N multiplication table in an Excel spreadsheet.
# For example, when the program is run like this:
#
# py multiplicationTable.py 6
#
# ... it should create a spreadsheet that looks like Figure 12-11.
#
# Row 1 and column A should be used for labels and should be in bold.

import openpyxl, sys
