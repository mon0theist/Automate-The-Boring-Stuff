#! /usr/bin/python
#
# ATBS Chapter 11 - Practice Project - Link Verification
#
# Write a program that, given the URL of a web page, will attempt to download
# every linked page on the page. The program should flag any pages that have a
# 404 “Not Found” status code and print them out as broken links.

# Testing
# Nonexistent Page: http://inventwithpython.com/page_that_does_not_exist
# Nonexistent URL: http://abcdefg.gov
# Page of Links: https://www.ucl.ac.uk/GeolSci/micropal/links.html

import requests, bs4, os

# Create folder for image downloads
os.makedirs('link_verification', exist_ok=True)

try:
    res = requests.get(input('Please enter a URL: '))
except requests.exceptions.ConnectionError:
    print('Connection Error: URL/Domain does not seem to exist')
    # This differs from the HTTPError of raise_for_status(), as the response object
    # can't be created in the first place if the initial requests.get() is called
    # on a URL that doesn't exist.
    # It seems HTTPError is for the case when the domain/site of the URL exists,
    # but the specific page does not (ie a 404 error). See example below.

print('Verifying download links on page...\n')

# taken from:
# https://2.python-requests.org//en/latest/user/quickstart/#errors-and-exceptions
try:
    res.raise_for_status()
except requests.exceptions.HTTPError:
    print('Error (404): Page does not seem to exist')
except requests.exceptions.Timeout:
    print('Error: Connection has timed out')
except requests.exceptions.TooManyRedirects:
    print('Error: Too many redirects')

soup = bs4.BeautifulSoup(res.text, features="lxml")
links = soup.select('a')

for i in range(len(links)):
    dl = links[i].get('href')
    try:
        print('Verifying: ' + str(dl))
        res = requests.get(dl)
    except requests.exceptions.InvalidSchema:
        print('Error: ' + str(dl) + ' has an invalid schema, might be a mailto email link')
    except requests.exceptions.MissingSchema:
        print('Invalid URL: ' + str(dl) + ' is not valid')
    except requests.exceptions.ConnectionError:
        print('Connection Error: URL/Domain "' + str(dl) + '"does not seem to exist')

    try:
        res.raise_for_status()
        linkfile = open(os.path.join('link_verification', os.path.basename(dl)), 'wb')
        for chunk in res.iter_content(100000):
            linkfile.write(chunk)
        linkfile.close()
        print('Success!\n')
    except IsADirectoryError:
        print('Ignoring: "' + str(linkfile) + '" is a directory')
    except TypeError:
        print('TypeError: ' + str(dl) + ' is not valid')
    except requests.exceptions.HTTPError:
        print('Error (404): Page does not seem to exist')
        print('Broken Link: ' + dl)
    except requests.exceptions.Timeout:
        print('Error: Connection has timed out')
    except requests.exceptions.TooManyRedirects:
        print('Error: Too many redirects')

print('Done!')
