# to read a file we need to use open(). this returns a variable called file handler, used to perform operations on file.

#handle = open(filename, mode) #Mode is opcional. If you plan to read, use 'r', and use 'w' if you want to write
#each line in file is treated as a sequence of strings, so if you want to print
name = input('Enter filename: ')
file = open(name, 'r')
#for word in file:
#    print(word)

    #How to read the whole file
readedFile = file.read()
#print(len(readedFile))
#Read all the stuff as a string
print(readedFile)

fhand = open('file.txt', 'r')
for line in fhand:
    if line.startswith('o fabin'):
        print(line)

        #to remove the double \n just use .rstrip() in print, like this: print(line.rstrip())
