import json

import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

sum = 0

info = json.loads(data)

comments = info['comments']

for item in comments:
    count = int(item['count'])
    sum = sum + count

print(sum)
