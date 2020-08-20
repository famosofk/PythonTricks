import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup as BS

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://globo.com'

handler = urllib.request.urlopen(url)
hand = handler.read()

soup = BS(hand, 'html.parser')

tags = soup('a')

for item in tags:
    print(item.get('href', None))

