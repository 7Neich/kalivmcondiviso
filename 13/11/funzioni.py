def saluta(nome):
    saluto = f"Ciao, {nome}!"
    return saluto

messaggio=saluta ("Alice")
print(messaggio)

def somma(a,b):
    return a + b
print(somma(3,30))

def saluta_antonio():
    return "Saluta Antonio"
print(saluta_antonio())

def mia_funzione():
    numero = 7
    print(numero)
mia_funzione()  #non è accessibile 
#print(numero)
#    
globale = 20
def stampa_1():
    global globale
    globale = 30
    print(globale)
def stampa_2():
    print(globale)

stampa_1()
stampa_2()

def saluta(nome,messaggio):
    print(f"{messaggio},{nome}!")

saluta(messaggio="hallo", nome="Alice")

def sottrazione(x,y):
    return x - y 
print(sottrazione(y=3,x=4))





