name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mDict = dict()

for line in handle:
    if line.startswith('From '):
        date = line.split()[5]
        day = date.split(':')[0]
        mDict[day] = mDict.get(day, 0) + 1

order = sorted( [ (k,v) for k,v in mDict.items()      ])
for k,v in order:
    print(k,v)
