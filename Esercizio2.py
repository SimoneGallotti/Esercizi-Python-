#Esercizio2

oreP = [10,11,13,15,17]
oreA = [12,14,16,18,20]
destinazioni = ["Roma", "Milano", "Torino", "Napoli", "Firenze"]

destinazione = int(input("Inserisci la destinazione: "))

indice = 0

for I in range(len(destinazioni)): 
    if(destinazione == destinazioni[i]): 
        indice = i
        break 

print(f"l'orario di partenza corrsispondete è: {oraP[indice]}")

print("Intervallo di tempo: ") 
n1 = int(input("Inserisci primo termine: "))
n2 = int(input("Inserisci secondo termine: "))

print("Nell'intervaòllo inserito partono: ")
for i in range(len(oreP)): 
    if( n1 < oreP[i] < n2): 
        print(f"Corsa {i} con destinazione{destinazioni[i]} con partenza e  arrivo{oreP[i]}")
