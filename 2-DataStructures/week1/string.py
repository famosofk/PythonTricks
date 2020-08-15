s = "string de teste"

print(s[3:7])
phrase = "Hi, my name is Bob".lower()
print(phrase)

s1 = phrase.find(' ', 7)
#Esse código procura por um espaço a partir da sétima letra
s2 = "my name is doctor q, mane"

print(s2.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

text = "X-DSPAM-Confidence:    0.8475";
start = text.find(':')
string = text[start+1:start+60]
print(string.strip())
