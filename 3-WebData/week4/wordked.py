import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#ignore ssl certificate names
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
url = 'http://' + url
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
val = list()

for tag in tags:
    string = str(tag)
    val = val + re.findall('[0-9]+', string)

total = 0
for item in val:
    total = total + int(item)
 
print(total)

    
    
    



'''
for tag in tags:
    val = str(tag)
    val = val.split('>')
    val = val[1].split('<')
    val = val[0]
    print(val)
    
'''
