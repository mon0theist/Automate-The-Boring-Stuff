#! /usr/bin/python
#
# ATBS - Chapter 17 - Identifying Photo Folders on the Hard Drive
#
# I have a bad habit of transferring files from my digital camera to temporary
# folders somewhere on the hard drive and then forgetting about these folders.
# It would be nice to write a program that could scan the entire hard drive and
# find these leftover “photo folders.”
#
# Write a program that goes through every folder on your hard drive and finds
# potential photo folders. Of course, first you’ll have to define what you
# consider a “photo folder” to be; let’s say that it’s any folder where more than
# half of the files are photos. And how do you define what files are photos?
#
# First, a photo file must have the file extension .png or .jpg. Also, photos are
# large images; a photo file’s width and height must both be larger than 500
# pixels. This is a safe bet, since most digital camera photos are several
# thousand pixels in width and height.
#
# When the program runs, it should print the absolute path of any photo folders
# to the screen.

# Provided skeleton in problem description was written for Windows but I will
# modify for Linux

import os
from PIL import Image

# constant, so that search path can be easily modified
SEARCH_FOLDER = os.path.abspath('/home/abdulhakeem/Pictures')
print('Search Folder: ' + str(SEARCH_FOLDER))

# results
folder_list = []

for foldername, subfolders, filenames in os.walk(SEARCH_FOLDER):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.endswith('.png') or filename.endswith('.jpg')):
            numNonPhotoFiles += 1
            continue    # skip to next filename

            # Open image file using Pillow.
            img_obj = Image.open(filename)
            img_obj_w, img_obj_h = img_obj.size

            # Check if width & height are larger than 500.
            if img_obj_w > 500 and img_obj_h > 500:
                # Image is large enough to be considered a photo.
                numPhotoFiles += 1
            else:
                # Image is too small to be a photo.
                numNonPhotoFiles += 1

        if numPhotoFiles >= (numNonPhotoFiles * 2):
            # check for duplicates
            if not os.path.abspath(foldername) in folder_list:
                folder_list.append(os.path.abspath(foldername))
                print(os.path.abspath(foldername))
