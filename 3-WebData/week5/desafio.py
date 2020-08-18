import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET

page = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_894243.xml').read()

tree = ET.fromstring(page)

list = tree.findall('.//count')

total = 0

for item in list:
    total = total + int(item.text)
    
print(total)