file = open('test.txt', 'w+')
file.write('It was a dark and stormy night when the one arrives')
print(file.read())
file.close()

with open('test.txt') as fis:
    print(fis.readline())
    #opening with w will delete the content, you must use 'a'