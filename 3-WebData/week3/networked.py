import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(( 'url', port ))
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
#manda o comando para o servidor.

while True:
    data = mysock.recv(512) # fica recuperando o que é enviado peo server
    if(len(data) < 1): # se vier vazio é pq acabou.
        break
    print(data.decode())
mysock.close()     # fecha a conexão
