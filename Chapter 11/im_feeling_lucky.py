#! /usr/bin/python
#
# ATBS Chapter 11 - I'm Feeling Lucky
#
# Tutorial is out of date, doesn't work anymore, not sure how to fix it

import requests, sys, bs4, webbrowser

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features='lxml') # creates BS4 object

# TODO: Open a browser tab for each result
# linkElems = soup.select('.r a') # may be out of date and need fixing
linkElems = soup.select('div r')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
