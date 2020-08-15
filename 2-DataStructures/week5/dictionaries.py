purse = dict()

purse['money'] = 12
purse['candies'] = 20
purse['tissues'] = 73
purse['tissues'] = purse['tissues'] + 5
print(purse)

print(len(purse))

# one way to count using dic is using the word as key and the value as number, such this counting names

names = dict()
names['amanda'] = 1
names['cleiton'] = 1
names['amanda'] = names['amanda'] + 1
names['cleiton'] = names['cleiton'] + 2
names.get('jorge', 1)
print(names)

#we can do a name reader like this
mdict = dict()
while (True):
    break;
    name = input("Name: ")
    if name == 'done' : break
    mdict[name] = mdict.get(name, 0) + 1
print(mdict)

#printing value
counts = {'chuck' : 12, 'fabiano' : 18, 'alice' : 15}
for name in counts:
    print(name, counts[name])
print(list(counts)) #this will print a list of the keys

# we can print the values and the keys by using two iterables variables
jjj = {'chuck' : 1, 'fred' : 2, 'cris' : 13}
for aaa,bbb in jjj.items():
    print(aaa, bbb)








#   Get dictionary method
# if name in dictionary:
#   x= dictionary[name]
# else
#   x = 0
#value = dictionary.get('name',0)
#
