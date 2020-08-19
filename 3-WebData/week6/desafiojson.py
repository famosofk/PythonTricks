import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_894244.json'

handler = urllib.request.urlopen(url)

data = handler.read().decode()

hand = json.loads(data)
dic = hand.get('comments', 0)
total = 0
for item in dic:
    total = total + int(item.get('count', 0))

print(total)

    

