#! /usr/bin/python
#
# ATBS - Chapter 15 - Scheduled Web Comic Downloader
#
# Write a program that checks the websites of several web comics and automatically
# downloads the images if the comic was updated since the program’s last visit.
# Your operating system’s scheduler (Scheduled Tasks on Windows, launchd on OS X,
# and cron on Linux) can run your Python program once a day. The Python program
# itself can download the comic and then copy it to your desktop so that it is
# easy to find. This will free you from having to check the website yourself to
# see whether it has updated.
#
# List of webcomics from https://automatetheboringstuff.com/list-of-web-comics.html
#
# http://www.lefthandedtoons.com/
# http://buttersafe.com/
# http://www.savagechickens.com/
# http://www.lunarbaboon.com/
# http://completelyseriouscomics.com/
# http://www.exocomics.com/
# http://nonadventures.com/
# http://moonbeard.com/
# http://www.happletea.com/
#
# Many of these comics don't have easily parsable URLs, can only do the ones that are similar to xkcd's,
# ie: http://xkcd.com/comicnumber
#
# To do the other ones would require a web crawler, which is beyond the scope of this book
#
# This was written on an Arch Linux system, so the schedling will be provided by
# the 'cronie' package. YMMV if you're on a different distro or OS.
# See: https://wiki.archlinux.org/index.php/Cron
#
# Copying and modifying the code from the XKCD Multi-Downloader from this chapter

import requests, os, bs4

# create comics folder and subfolders
os.makedirs('comics/lefthandedtoons', exist_ok=True)
os.makedirs('comics/completelyseriouscomics', exist_ok=True)
os.makedirs('comics/exocomics', exist_ok=True)
os.makedirs('comics/xkcd', exist_ok=True)

def download_xkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic + 1):
        # Download the page
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image')
        else:
            comicURL = comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comicURL))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

def download_lefthanded(start_comic, end_comic):
    for url_number in range(start_comic, end_comic + 1):
        # download the page
        print('Downloading page: http://www.lefthandedtoons.com/%s...' % (url_number))
        res = requests.get('http://www.lefthandedtoons.com/%s...' % (url_number))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # find the URL of the comic image
        comic_elem = soup.select('.comicimage')
        if comic_elem = []:
            print('Could not find comic image...')
        else:
            comic_url = comic_elem[0].get('src')
            print('Downloading image %s...' % (comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

        # save image file to ./comics/lefthandedtoons
        image_file = open(os.path.join('lefthandedtoons', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
                image_file.write(chunk)
        image_file.close()

def download_completelyseriouscomics(start_comic, end_comic):
    for url_number in range(start_comic, end_comic + 1):
        # inconsistent URLs
        # try downloading the page
        try:
            print('Downloading page: http://completelyseriouscomics.com/?p=%s' & (url_number))
            res = requests.get('http://completelyseriouscomics.com/?p=%s' % (url_number))
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            print('404: No comic found at url number: %s' % (url_number))
            continue

        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of the comic image
        comic_elem = soup.select('.comicpane img')
        if comic_elem = []:
            print('No comic image found')
        else:
            comic_url = comic_elem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            # save the image to ./comics/completelyseriouscomics
            image_file = open(os.path.join('completelyseriouscomics', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

def download_exocomics(start_comic, end_comic):
    for url_number in range(start_comic, end_comic + 1):
        # download the page
        print('Downloading page https://www.exocomics.com/%s' % (url_number))
        res = requests.get('https://www.exocomics.com/%s' % (url_number))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # find the URL of the comic image
        comic_elem = soup.select('.image-style-main-comic')
        if comic_elem == []:
            print('Could not find comic image')
        else:
            comic_url = comic_elem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            # save the image to ./comics/exocomics
            image_file = open(os.path.join('exocomics', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(10000):
                image_file.write(chunk)
            image_file.close()

# TODO: figure out how to only check for new comics, instead of re-downloading
# the entire site each time
