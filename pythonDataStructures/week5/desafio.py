name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mDict = dict()
for line in handle:
    if line.startswith('From '):
        email = line.split()[1]
        mDict[email] = mDict.get(email, 0) + 1

moretimes =0
word = ""

for k,v in mDict.items():
    if v > moretimes:
        moretimes = v
        word = k
print(moretimes, word)
