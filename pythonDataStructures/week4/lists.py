#Manipulating lists



a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))
d = range(6)
print(d)
#to get the first 3
d = c[:3]
c.insert(3, 76) #Primeiro a posição e depois o item
c.sort()

print(c)

# we can create an empty list and add items to it using this

listagem = list()
listagem.append("fabin")
print(listagem)


abc = "One two three"
stuff = abc.split()
#Splits by defautl whitespace but you can choose which caracter use, such as split(',')

#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line check to see if the word is already in the list and if not
#append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
mlist = list()
for line in fh:
    line = line.rstrip()
    aux = line.split()
    for word in aux:
        if word  in mlist: continue
        mlist.append(word)
mlist.sort()
print(mlist)
