#! /usr/bin/python
#
# ATBS Chapter 11 - Practice Projects - Image Site Downloader
#
# Write a program that goes to a photo-sharing site like Flickr or Imgur,
# searches for a category of photos, and then downloads all the resulting images.
# You could write a program that works with any photo site that has a search feature.

# Pseudocode
# Determine starting URL
# Create folder for image downloads
# Open site, navigate to URL (selenium)
# enter search query (selenium)
# download page that resulted from search query (requests)
# parse page for <img> tags (beautifulsoup)
# download images from links listed in <img> tags (res.iter_content, probably needs a loop)


from selenium import webdriver
import webbrowser, requests, os, bs4

url = 'https://imgur.com'
# imgur url search structure: https://imgur.com/search?q=[search term]
# multiple search terms: https://imgur.com/search/score?q=cats+and+babies

os.makedirs('image_site_downloader', exist_ok=True)
