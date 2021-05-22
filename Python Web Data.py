import socket
socket.getaddrinfo('127.0.0.1', 25)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ("http://data.pr4e.org", 25))
cmd = "GET http://data.pr4e.org/romeo-full.txt".encode() #encode takes string and changes into bytes
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)< 1):
        break
    print(data.decode()) #it converts bytes into string
mysock.close()
 #end

#next way for the socket programme above
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo-full.txt")
for line in fhand:
    print(line.decode().strip())

import urllib.request, urllib.parse, urllib.error
ola = input("A URL")
fhand = urllib.request.urlopen(ola)
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word]= counts.get(word, 0 ) + 1
print(counts)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input("URL")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
#retrive all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get("href", None))