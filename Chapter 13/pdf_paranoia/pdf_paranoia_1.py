#! /usr/bin/python
#
# ATBS - Chapter 13 - PDF Paranoia (Part 1)
#
# (Part 1)
# Using the os.walk() function from Chapter 9, write a script that will go through
# every PDF in a folder (and its subfolders) and encrypt the PDFs using a password
# provided on the command line. Save each encrypted PDF with an _encrypted.pdf
# suffix added to the original filename. Before deleting the original file, have
# the program attempt to read and decrypt the file to ensure that it was encrypted
# correctly.
#
# (Part 2)
# Then, write a program that finds all encrypted PDFs in a folder (and its subfolders)
# and creates a decrypted copy of the PDF using a provided password. If the password
# is incorrect, the program should print a message to the user and continue to
# the next PDF

import os, sys, PyPDF2

# create empty pdf list
pdf_list = []

# walk current directory for pdfs
print('Searching for PDFs...')
for rootfolder, subfolder, file in os.walk(os.getcwd()):
    for i in range(len(file)):
        if file[i].endswith('.pdf'):
            pdf_list.append(file[i])
            print('Found: ' + str(file[i]))

# loop over pdf_list and encrypt
print('Encrypting PDFs...')
for i in range(len(pdf_list)):
    file = open(pdf_list[i], 'rb')
    pdf_reader = PyPDF2.PdfFileReader(file)
    pdf_writer = PyPDF2.PdfFileWriter()
    # adding pages to pdfwriter object
    for pagenum in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(pagenum))
    pdf_writer.encrypt(str(sys.argv[1]))
    # os.path.splitext to get filename without extension
    cryptpdf = open(os.path.splitext(pdf_list[i])[0] + '_encrypted.pdf' ,'wb')
    pdf_writer.write(cryptpdf)
    # close files
    cryptpdf.close()
    file.close()
    # verify
    print('Verifying encrypton...')
    crypt_reader = PyPDF2.PdfFileReader(open(os.path.splitext(pdf_list[i])[0] + '_encrypted.pdf', 'rb'))
    if crypt_reader.isEncrypted == True:
        crypt_reader.decrypt(str(sys.argv[1]))
        try:
            crypt_reader.getPage(0)
            print('Encryption confirmed: ' + os.path.splitext(pdf_list[i])[0] + '_encrypted.pdf')
        except PyPDF2.utils.PdfReadError:
            print('Error: ' + str(pdf_list[i]) + ' was not successfully decrypted')
            continue

# delete unencrypted pdfs
print('Deleting unencrypted PDFs...')
for i in range(len(pdf_list)):
    os.unlink(pdf_list[i])
    print('Deleted: ' + str(pdf_list[i]))
