import random

print(f"Genera un nome per la tua Band")

città=input("Dove sei nato?: ").strip().lower()
animale=input("il nome del tuo animale domestico?: ").strip().lower()


nome_band = città + "" + animale

while True:
    pool_parole = ["Steigend", "Mystisch", "Groove", "Stimmung", "Echo", "Die", "Projekt", "Gruppe", "Vermächtnis"]



    new_parole = random.choice(pool_parole)


    if città == "roma":
        opzione_1 = f"Roman {new_parole} {animale}"
        opzione_2 = f"Gladiators of {new_parole}"
        opzione_3 = f"{animale} of the Seven Hills"

    elif città == "milano":
        opzione_1 = f"Milano {new_parole} Vibes{animale} "
        opzione_2 = f"The Fashion {animale}{città}s"
        opzione_3 = f"Milan {new_parole} Squad"
    elif città == "Bologna":
        opzione_1 =f"Tortelini {new_parole}{città} Punks"
        opzione_2 = f"Lasagne {animale} crude"
        opzione_3 = f"Torre {new_parole}{città} "
    else:
        opzione_1 = f"{new_parole} {città} {animale}"
        opzione_2 = f"{città} {animale} {new_parole}"
        opzione_3 = f"{new_parole} {animale} of {città}"    


    nome_band = random.choice([opzione_1, opzione_2, opzione_3])


    print(f"il nome della tua band è: {nome_band}")

    risposta = input("Andava bene?(si/no): ").strip().lower()

    if risposta == "si":
        print("8ttimo")
        break
    else:
        print("Inserire solo si o no!!!! altrimenti non funziona, rilancia ;)")






