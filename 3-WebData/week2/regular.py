import re

x = "My 2 favourite numbers are 19 and 32"
val = re.findall('[0-9]+', x)
print(val)
vowels = re.findall('[AEIOU]+', x)
#Using [0-9] procura por números
#Using [AEIOU] it looks for any uppercase vowels
#adding ? at the end, like this '^F.+:?' it won't be greedy

'''
handler = open('mbox-short.txt')

for line in handler:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)

#using regularExpression

for line in handler:
    line = line.rstrip()
    if re.search('^From: ', line):
        print(line)

#this method substitutes the startswith method.


for line in handler:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print(line)
#. means any character and * means 0 or more times. This looks for lines that starts with X followed by any character followed by
#any number os characters and has a collon
#if re.search('^X.*/S+:', line):/S means that can't have whitespace + means one or more times

'''
