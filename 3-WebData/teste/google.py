'''
import urllib.parse, urllib.request, urllib.error
import ssl
from bs4 import BeautifulSoup as BS

sourcesList = ['http://br.financas.yahoo.com', 'http://infomoney.com.br']

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Entre o site que deseja buscar: ')
url = 'http://' + url

termo = input('Entre o termo que deseja procurar: ')

hand = urllib.request.urlopen(url).read()
print('')

soup = BS(hand, 'html.parser')
links = soup('a')

for item in links:
    if item.get('href', 0).find(termo) > 0:
        print(item.get('title', 0), '\n' )
        print( item.get('href', 0), '\n\n')

        '''


import urllib.parse, urllib.request, urllib.error
import ssl
from bs4 import BeautifulSoup as BS

sourcesList = ['http://br.financas.yahoo.com', 'http://infomoney.com.br']

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


termo = input('Entre o termo que deseja procurar: ')

for sources in sourcesList:

    hand = urllib.request.urlopen(sources).read()
    print('')
    soup = BS(hand, 'html.parser')
    links = soup('a')

    for item in links:
        if item.get('href', 0).find(termo) > 0:
            print(item.get('title', 0), '\n\n')
            print(item.get('href', 0), '\n')
