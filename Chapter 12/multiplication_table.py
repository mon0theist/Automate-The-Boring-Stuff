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
from openpyxl.utils import get_column_letter, column_index_from_string
# DEPRECATED:
# from openpyxl.cell import get_column_letter, column_index_from_string

# Pseudocode
# Create workbook, set sheet
# N = sys.argv[1]
# Check if N = int, otherwise error
# rows = N
# column_letter = get_column_letter(N)
# minimum cell = ['A1']
# maximum cell = [(get_column_letter(N) + str(N)]
#
# Figure out loop
# for rows in range(1, N):
#   for columns in range(1, N):
#
#
# row = i
# column = j


# Create workbook, set sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Determine N
N = sys.argv[1]
if not type(N) == int:
    print('Invalid argument: Please enter an int value\n')
    exit()
else:
    # write cells
    
