lista = [1, "ciao", 3.14, [1,2,3],(18.3839,80.78728),{"nome":"pinco","cognome": "Pallino"}]
print(lista[0])
print(lista[1])
print(lista[3][1])
print(lista[4][0])
print(lista[5]["cognome"])

lista.append("Ciao")
print(lista)
lista.insert(2,"ciao")
print(lista)
lista.pop()
print(lista)
del lista[0]
print(lista)
