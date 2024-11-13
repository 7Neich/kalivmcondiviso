dizionario = {"nome": "Greta", "cognome":"Levi","età":23}
print(dizionario)
print(dizionario["nome"])
print(dizionario["età"])
print(dizionario)

dizionario["età"] = 24

print(dizionario)
#del dizionario["età"]
print(dizionario)

dizionario.pop("età")
print(dizionario)
print(dizionario.values())
print(dizionario.keys())
