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
#
# sheet.cell(row=i, column=j).value
#
# Excel Formula:
# =[cell]*[cell]
#
# Outer Loop (for each column):
#   Inner Loop (for each row in each column)


# Create workbook, set sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Determine N
n = sys.argv[1]
if not type(n) == int:
    print('Invalid argument: Please enter an int value\n')
    exit()
else:
    # Cell A1 should be blank
    sheet.cell(row=1, column=1).value = 'BLANK'

    # create x-axis (row 1, columns 2 thru n)
    for i in range(2, n+2):
        sheet.cell(row=1, column=i).value = str(i - 1)
        #TESTING print(sheet.cell(row=1, column=i).value)
        # figure out how to set text as Bold and Centered

    # create y-axis (column 1/A, rows 2 thru n)
    for i in range(2, n+2):
        sheet.cell(row=i, column=1).value = str(i - 1)
        #TESTING print(sheet.cell(row=i, column=1).value)
        # figure out how to set text as Bold and Centered

    # write cells
    # for each row (i) (starting with B):
    #   loop from (i)(2) to (i)(end of row)
    # sheet.max_column
    for i in range(2, (sheet.max_column + 1):
        for j in range(2, ):
