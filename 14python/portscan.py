import socket as so

target = input ("inserisci l'indirizzo da scansire: ")
portrange = input("inserisci porta minima e porta massima nel formato min-max es [5-200]")

lport = int(portrange .split('-')[0])
hport = int(portrange .split('-')[1])


print("Scansione in corso di",target, "dalla porta",lport,"alla porta",hport)

for port in range(lport,hport+1):
    s = so.socket(so.AF_INET,so.SOCK_STREAM)
    status = s.connect_ex(target,port)
    chiuse = ""
    if(status == 0):
        print('*** Porta' port, '-APERTA ***')
    else:
        chiuse = f"{chiuse} {port}"

print(f"Porte chiuse: {chiuse}")
s.close()
