#! /usr/bin/python
#
# ATBS - Chapter 17 - Extending and Fixing the Chapter Project Programs
# Resize and Add Logo (Fixed)
#
# The resizeAndAddLogo.py program in this chapter works with PNG and JPEG files,
# but Pillow supports many more formats than just these two. Extend resizeAndAddLogo.py
# to process GIF and BMP images as well.
#
# Another small issue is that the program modifies PNG and JPEG files only if
# their file extensions are set in lowercase. For example, it will process zophie.png
# but not zophie.PNG. Change the code so that the file extension check is case
# insensitive.
#
# Finally, the logo added to the bottom-right corner is meant to be just a small
# mark, but if the image is about the same size as the logo itself, the result
# will look like Figure 17-16. Modify resizeAndAddLogo.py so that the image must
# be at least twice the width and height of the logo image before the logo is pasted.
# Other wise, it should skip adding the logo.
#
# Resized catlogo.png to 150x150: catlogo_resized_150x150.png

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo_resized_150x150.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
print('Logo dimensions: %sx%s\n' % (logoWidth, logoHeight))
# width, height of catlogo.png should normally be 808(W)x768(H)
# however this is too large to fit in the SQUARE_FIT_SIZE value of 300, so I'm
# resizing the catlogo.png to 150x150

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') \
    or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp')) \
    or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size
    # check if image is twice as big as logo (1616x1536)
    if (width >= (logoWidth * 2) and height >= (logoHeight * 2)):
        # Check if image needs to be resized
        if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
            # calculate the new width and height to resize to
            if width > height:
                height = int((SQUARE_FIT_SIZE / width) * height)
                width = SQUARE_FIT_SIZE
            else:
                width = int((SQUARE_FIT_SIZE / height) * width)
                height = SQUARE_FIT_SIZE

            # resize the image
            print('Resizing %s...' % (filename))
            im = im.resize((width, height))

            # Add the logo
            print('Adding logo to %s...' % (filename))
            im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

            # Save changes
            im.save(os.path.join('withLogo', filename))
    else:
        print('Skipping image: %s...image is not 2x size of logo' % (filename))
