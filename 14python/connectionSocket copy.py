import socket as so
SRV_ADDR = "" # in questo se vuoto utilizza tutte le interfacce, altrimenti quella di appartenenza della famiglia
SRV_PORT = 4444
s =  so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT)) 
s.listen(1)
print("Sto attendendo una connessione...") 
connection, address = s.accept()
print("ho stabilito una connessione con: ", address)
while True:
    connection.sendall(b"$ ")
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b"ho ricevuto il messaggio! \n")
    print(data.decode('utf-8'))
connection.close()


