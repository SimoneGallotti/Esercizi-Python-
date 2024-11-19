import math 

print("Questo programma calcola la media di tre voto in trentesimi.")
voto1 = int(input("Inserire il primo voto: "))
voto2 = int(input("Inserire il secondo voto: "))
voto3 = int(input("Inserire il terzo voto: "))

selezione = int(input("Inserire 1 se si vuole la media in trentesimi o inserire 2 se si vuole la media in centesimi: "))

if (selezione == 1):
    media = (voto1 + voto2 + voto3)/3
    print (f"La media calcolata in treseimi è uguale a: {round(media, 2)}.")
elif (selezione == 2):
    media = ((voto1 + voto2 + voto3)/3)*100/30
    print (f"La media calcolata centesimi è uguale a: {round(media, 2)}.")
else: 
    print ("E' stato inserito un valore non corretto.")
