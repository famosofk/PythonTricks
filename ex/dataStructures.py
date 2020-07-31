#tuples

x = ('string', 3, 7, 'bh', 89)
print(type(x))
#tuples are imatuble. This is a list of different types object. We create tuples using (). In python this would be listof

y = ["fabin", 3, "diretoria", 8, 73]
y.append("banana")
print(type(y))
#lists are mutable tuples. We create lists using []

#both of them are iterable so we can do this
for element in x:
    print(element)
#We can access elements using index as well. To do this you can simply use brackets y[3]
#to discover the length of a list or tuple we can use length. 
# Operation: + concatenate lists. * repeats the list

#Dictionaries are collections of objects with key and value. They don't have index and we create them with curly braces

dic = {"fabiano" : "fabiano.junior@nobugs.com.br", "jace" : "jacevenator@gmail.com"}
nome, sobrenome = dic
print(dic[nome])
