import re

handler = open('regex_sum_894239.txt')
lines = handler.read()
val = re.findall('[0-9]+', lines)
total = 0
for item in val:
    total = total + int(item)
print(total)