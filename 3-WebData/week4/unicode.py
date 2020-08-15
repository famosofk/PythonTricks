#since http is common, we have a lib that makes requests for us

import urllib.request, urllib.parse, urllib.error


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())