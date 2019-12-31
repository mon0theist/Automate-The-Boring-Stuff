#! /usr/bin/python
#
# ATBS Chapter 11 - Practice Projects - Image Site Downloader
#
# Write a program that goes to a photo-sharing site like Flickr or Imgur,
# searches for a category of photos, and then downloads all the resulting images.
# You could write a program that works with any photo site that has a search feature.

# Pseudocode
# import modules
# Create folder for image downloads
# Construct URL using search term(s) from command line (sys.argv[1:])
# download page that resulted from search query (requests)
# raise for status
# parse page for <img> tags (beautifulsoup)
# download images from links listed in <img> tags (res.iter_content, probably needs a loop)

# import modules
import requests, os, bs4, sys

# Create folder for image downloads
os.makedirs('image_site_downloader', exist_ok=True)

# Use search term(s) from command line (sys.argv[:end])
# usage: python image_site_downloader.py [term] [term] [term]
# imgur url search structure: https://imgur.com/search?q=[search term]
# multiple search terms: https://imgur.com/search/score?q=[term]+[term]+[term]
res = requests.get('https://imgur.com/search?q=' + '+'.join(sys.argv[1:]))
try:
    res.raise_for_status()
except requests.exceptions.InvalidURL:
    print('Error: Invalid URL')

# parse page for <img> tags (beautifulsoup)
soup = bs4.BeautifulSoup(res.text, features='lxml')
imgs = soup.select('img')

# download images from links listed in <img> tags (res.iter_content, probably needs a loop)
# for every item in imgs[], download the src attr
if imgs == []:
    print('Could not find any images.')
else:
    for i in range(len(imgs)):
        # a = imgs[i].get('src')
        imglink = 'http:' + imgs[i].get('src')
        res = requests.get(imglink)
        imgfile = open(os.path.join('image_site_downloader', os.path.basename(imglink)), 'wb')
        print('Downloading ' + os.path.basename(imglink) + '...')
        for chunk in res.iter_content(100000):
            imgfile.write(chunk)
        imgfile.close()

print('Done!')
