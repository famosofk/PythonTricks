import sqlite3
#faz a conexão com o banco de dados
conn = sqlite3.connect('emaildb.sqlite')
#cria o ponteiro para operar o banco
cur = conn.cursor()
#Se existir a tabela que vamos usar, exclui ela
cur.execute('''Drop table if exists Counts''')
cur.execute('''Create table Counts(email TEXT, count INTEGER)''')
fname = input('Enter the file name: ')
if(len(fname)<1): fname = 'mbox.txt'
#abre o documento
fh = open(fname)
for line in fh:
    #Se não começar com From não tem email, então pula
    if not line.startswith('From: ') : continue
    pieces = line.split()
    #Selecionando o email
    email = pieces[1]
    #Apontamos para quanto emails temos 
    cur.execute('''Select count from Counts where email=?''', (email,))
    #Recuperamos o valor da coluna
    row = cur.fetchone()
    if row is None:
        #Caso não aponte para nada, criamos uma coluna com 1 email
        cur.execute('''Insert into Counts (email, count) values (?, 1)''', (email,))
    else:
        cur.execute('''Update Counts set count = count + 1 where email=?''', (email,))
    conn.commit()
sqlstring = 'Select email, count from Counts ORDER BY count DESC limit 10'
for row in cur.execute(sqlstring):
    print(str(row[0]), row[1])

