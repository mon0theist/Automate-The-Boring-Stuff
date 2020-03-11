#! /usr/bin/python
#
# ATBS Chapter 14 - Practice Projects - excel_to_csv_converter.py
#
# Excel can save a spreadsheet to a CSV file with a few mouse clicks, but if you
# had to convert hundreds of Excel files to CSVs, it would take hours of clicking.
# Using the openpyxl module from Chapter 12, write a program that reads all the
# Excel files in the current working directory and outputs them as CSV files.
#
# A single Excel file might contain multiple sheets; you’ll have to create one
# CSV file per sheet. The filenames of the CSV files should be
# <excel filename>_<sheet title>.csv, where <excel filename> is the filename of
# the Excel file without the file extension (for example, 'spam_data', not 'spam_data.xlsx')
# and <sheet title> is the string from the Worksheet object’s title variable.
#
# Download the ZIP file excelSpreadsheets.zip from http://nostarch.com/automatestuff/,
# and unzip the spreadsheets into the same directory as your program. You can use
# these as the files to test the program on.
#
# See example skeleton below

import csv, openpyxl, os, pprint

for excel_file in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excel_file.endswith('.xlsx'):
        continue
    wb = openpyxl.load_workbook(excel_file)

    for sheet_name in range(len(wb.sheetnames)):
        # Loop through every sheet in the workbook.
        sheetname = wb.sheetnames[sheet_name]
        sheet_obj = wb[sheetname]

        # Create the CSV filename from the Excel filename and sheet title.
        csv_filename = str(os.path.basename(excel_file + '_' + sheetname + '.csv'))

        # Create the csv.writer object for this CSV file.
        output_file = open(csv_filename, 'w', newline='')
        output_writer = csv.writer(output_file)

        # Loop through every row in the sheet.
        for row_num in range(1, sheet_obj.max_row + 1):
            row_data = []
            # Loop through each cell in the row.
            for col_num in range(1, sheet_obj.max_column + 1):
                # Append each cell's data to row_data.
                row_data.append(sheet_obj.cell(row=row_num, column=col_num).value)

            # Write the row_data list to the CSV file.
            for row in row_data:
                output_writer.writerow(row)

        output_file.close()
