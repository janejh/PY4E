import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

sum = 0

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
    
resultslist = tree.findall('comments/comment') #get all the tags, the full <comment></comment> tags, thus a list
    
for results in resultslist:
    num = results.find('count').text
    sum = sum + int(num)
    
print(sum)
