#! /usr/bin/python
#
# ATBS Chapter 11 - XKCD Downloader

import requests, os, bs4

url = 'http://xkcd.com' # starting URL
os.makedirs('xkcd', exist_ok=True) # store coics in ./xkcd
while not url.endswith('#'):
    # Download the page
    print('Downloading the page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='lxml')

    # Find the URL of the comic in the page
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        except requests.exceptions.InvalidURL:
            # skip this comic
            # there's an invalid URL that comes up, something about "challenger"
            # had to add thise exception to skip it
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

        # Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')


Print('Done!')
