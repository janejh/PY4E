# Following Links in Python

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter Count: ')
count = int(count)
position = input('Enter Position: ')
position = int(position)

# Retrieve all of the anchor tags

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print(tags[position - 1].contents[0])
    url = tags[position - 1].get('href', None)
    count = count - 1
