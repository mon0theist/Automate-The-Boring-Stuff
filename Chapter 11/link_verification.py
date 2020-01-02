#! /usr/bin/python
#
# ATBS Chapter 11 - Practice Project - Link Verification
#
# Write a program that, given the URL of a web page, will attempt to download
# every linked page on the page. The program should flag any pages that have a
# 404 “Not Found” status code and print them out as broken links.

import requests, bs4

res = requests.get(input('Please enter a URL: '))

try:
    res.raise_for_status()
except Exception as exc:
    print('Error: %s' % (exc))
