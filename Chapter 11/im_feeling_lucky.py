#! /usr/bin/python
#
# ATBS Chapter 11 - I'm Feeling Lucky
#
# Tutorial is out of date, doesn't work anymore, not sure how to fix it
# I can get BeautifulSoup to find regular tags like <a> or <p> but it won't pick
# up anything with a class or id. Can't figure out why.
#
# Test URL: https://www.google.com/search?q=Beautiful%20Soup

import requests, sys, bs4, webbrowser

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='lxml') # creates BS4 object

# TODO: Open a browser tab for each result
# this part doesn't seem to work, not sure why
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems)) # 5 or less search results
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
