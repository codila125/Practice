#!/usr/bin/env python3
import re
import requests
from bs4 import BeautifulSoup

site = input("Enter the URL")
site = str(site)

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
        print("Regex didn't match with the url: {}".format(url))
        continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative
            # if it is provide the base url which also happens
            # to be the site variable atm.
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)

import pytube
from pytube import YouTube
url = input("Enter the url")
url = str(url)
s = input("Audio or Video")
s = str(s)
if s=="Audio" or s=="audio":
    YouTube(url).streams.get_audio_only().download(output_path="/home/pralaxy/Downloads")
elif s=="Video" or s=="video" or s=="vdo":
    YouTube(url).streams.get_highest_resolution().download(output_path="/home/pralaxy/Downloads")



