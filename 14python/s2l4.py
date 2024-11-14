import math

print("Scegli la figura per calcolare il perimetro o circonferenza: ")
print("1. Quadrato")
print("2. Cerchio")
print("3. Rettangolo")

scelta = input("Inserisci il numero della tua scelta: ")

if scelta == "1":
    lato = float(input("Lato del quadrato: "))
    print("Perimetro:", lato * 4)

elif scelta == "2":
    raggio = float(input("Raggio del cerchio: "))
    print("Circonferenza:", 2 * math.pi * raggio)

elif scelta == "3":
    base = float(input("Base del rettangolo: "))
    altezza = float(input("Altezza del rettangolo: "))
    print("Perimetro:", 2 * (base + altezza))

else:
    print("Scelta non valida.")