import sqlite3

conn = sqlite3.connect('desafio1.sqlite')
cur = conn.cursor()

cur.execute('drop table if exists Ages')
cur.execute('Create table Ages(name varchar(128), age integer)')

cur.execute('delete from Ages')
cur.execute('''Insert into Ages (name, age) values ('Madelyn', 17)''')
cur.execute('''Insert into Ages (name, age) values ('Debbie', 333)''')
cur.execute('''Insert into Ages (name, age) values ('Laoise', 36)''')
cur.execute('''Insert into Ages (name, age) values ('Kodie', 18)''')
cur.execute('''Insert into Ages (name, age) values ('Clyde', 27)''')
cur.execute('''Insert into Ages (name, age) values ('Yishuka', 14)''')
conn.commit()
testeString = '53656C696E613333'
cur.execute('''select hex(name||age) as X from Ages order by X''')

for row in cur.execute('Select * from Ages'):
    cur.execute('''Update Ages set X = ? where X = ?''', (testeString, str(row[0]) ) )