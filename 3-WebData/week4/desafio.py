import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

position = 1
counter = 0
url = 'http://py4e-data.dr-chuck.net/known_by_Carra.html'
name = 'Carra'
while True:
    if counter == 7 : break
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        if position == 18:
            #print(tag.get('href', None))
            url = tag.get('href', None)
            val = url.split('_')[2]
            name = val.split('.')[0]
            counter = counter +1
            position = 1
            break
        position = position + 1
print(name)
        