#! /usr/bin/python
#
# ATBS - Chapter 17 - Custom Seating Cards
#
# Chapter 13 included a practice project to create custom invitations from a list
# of guests in a plaintext file. As an additional project, use the pillow module
# to create images for custom seating cards for your guests. For each of the
# guests listed in the guests.txt file from the resources at
# http://nostarch.com/automatestuff/, generate an image file with the guest name
# and some flowery decoration. A public domain flower image is available in the
# resources at http://nostarch.com/automatestuff/.
#
# To ensure that each seating card is the same size, add a black rectangle on the
# edges of the invitation image so that when the image is printed out, there will
# be a guideline for cutting. The PNG files that Pillow produces are set to 72
# pixels per inch, so a 4×5-inch card would require a 288×360-pixel image.

from PIL import Image, ImageDraw
import os

# create folder for invitations
os.makedirs('Invitations', exist_ok=True)

# load guests.txt into list (splitlines)
guest_file = open('guests.txt', 'r')
guest_list = guest_file.read().splitlines()
guest_file.close()

# load flower image
flower_img = Image.open('flower.jpg')
flower_width, flower_height = flower_img.size

# iterate over list:
for i in range(len(guest_list)):
    # generate image file of correct size
    img = Image.new('RGBA', (600, 600), 'white')
    # paste flower image onto invitation image
    img.paste(flower_img, (0, 0))
    # draw text onto image file (ImageDraw)
    draw = ImageDraw.Draw(img)
    draw.text((50, 100), "Hey " + guest_list[i] + ",\nYou're Invited!", fill='white')
    # add black rectangles to edges of images for cutting
    # draw.rectangle(xy, fill, outline)
    draw.rectangle((0, flower_height, flower_width, 600), 'black', 'black')
    draw.rectangle((flower_width, 0, 600, 600), 'black', 'black')
    img.save(os.path.join('./Invitations', guest_list[i] + '_invitation.png'))
    print('Saving file...: ' + guest_list[i] + '_invitation.png')

print('Done!')
