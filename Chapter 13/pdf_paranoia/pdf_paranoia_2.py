#! /usr/bin/python
#
# ATBS - Chapter 13 - PDF Paranoia (Part 2)
#
# (Part 1)
# Using the os.walk() function from Chapter 9, write a script that will go through
# every PDF in a folder (and its subfolders) and encrypt the PDFs using a password
# provided on the command line. Save each encrypted PDF with an _encrypted.pdf
# suffix added to the original filename. Before deleting the original file, have
# the program attempt to read and decrypt the file to ensure that it was encrypted
# correctly.
#
# (Part 2)z
# Then, write a program that finds all encrypted PDFs in a folder (and its subfolders)
# and creates a decrypted copy of the PDF using a provided password. If the password
# is incorrect, the program should print a message to the user and continue to
# the next PDF

import os, sys, PyPDF2

# create empty pdf list
pdf_list = []

# walk current directory for pdfs
print('Searching for PDFs ending with "_encrypted.pdf"...')
for rootfolder, subfolder, file in os.walk(os.getcwd()):
    for i in range(len(file)):
        if file[i].endswith('_encrypted.pdf'):
            pdf_list.append(file[i])
            print('Found: ' + str(file[i]))

# loop over pdf_list and decrypt
print('Decrypting PDFs...')
password = input('Please enter password: ')
for i in range(len(pdf_list)):
    file = open(pdf_list[i], 'rb')
    pdf_reader = PyPDF2.PdfFileReader(file)
    pdf_writer = PyPDF2.PdfFileWriter()
    if pdf_reader.decrypt(password) == 0:
        print('Decryption failed: ' + str(pdf_list[i]))
    elif pdf_reader.decrypt(password) == 1:
        for pagenum in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(pagenum))
        # create decrypted file, save to hard drive
        decryptpdf = open(os.path.splitext(pdf_list[i])[0] + '_decrypted.pdf' ,'wb')
        pdf_writer.write(decryptpdf)
        # close files
        decryptpdf.close()
        file.close()

print('Done!')
