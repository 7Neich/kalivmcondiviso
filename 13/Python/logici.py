if (1 < 3): print("vero")
if (1 > 3): 
    print ("non stampa") #questo perchè falso
else:
    print("False")
if (1 <= 1): print ("Vero")
if(1 >= 1): print("Vero")
if(2 != 1): print ("Vero")
if(2 != "Uno"): print("Vero")
if(1 == 1): print("Vero")

if(type(1) is int): print ("è un intero")
if(type("Ciao ") is not int ): print("Non è un intero")

lista = [1,2,3,"Pippo"]
if("Pippo"in lista): print("Pippo è in lista")
if("Fra"not in lista): print("Fra non è in lista")
if(not 1 > 1): print("nego la maggioranza")
if ((1 > 1) or (2 == 2)): print("la seconda è vera") 
if ((1 == 1) and ("Pippo" == "Pippo")) : print("sono entrambe vere")




