x = ('Glen', 'Cleiton', 'Roger')

#this is a tuple.

#sorted return the values as tuples

d = { 'a': 10, 'b':220, 'c':230}
t = sorted(d.items())
print(t)
#to sort by value you must use value, key instead of key, values
temporaryList = list()
for k,v in d.items():
    temporaryList.append( (v, k) )
list = sorted(temporaryList, reverse=True)
print( list )

c = {'a':10, 'b':15, 'c':22}
print( sorted( [ (v, k) for k, v in c.items() ] ) )

#List comprehension creates dynamics lists

print(sorted( [ i for i in range(75)], reverse=True     ))
