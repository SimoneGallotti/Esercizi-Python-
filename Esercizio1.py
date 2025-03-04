#Esercizio1
città = ["Milano", "Roma", "Napoli", "Torino"]
tmax = [28, 31, 34, 27]
tmin = [18, 21, 24, 17]

print("Programma calcola temperature.")

sommaTmax = 0 
sommaTmin = 0

for i in range(len(città)): 
    sommaTmax += tmax[i]
    sommaTmin += tmin[i]

mediaTmax = sommaTmax/len(tmax)
mediaTmin = sommaTmin/len(tmin)
print(f"Media temperature massime: {mediaTmax}")
print(f"Media temperature minime: {mediaTmin}")

print("Elenco città con temperature minime inferiore alla media: ")
for i in range(len(città)): 
    if(tmin[i] < mediaTmin): 
        print(città[i])

controllo = False

cittàUtente = str(input("Inserisci una città per verificare se è presente nella lista: "))
for i in range(len(città)): 
    if(città[i] == cittàUtente): 
        controllo = True
        break

if(controllo): 
    print("La città inserita è presente.")
else: 
    print("La città inserita non è presente. ")

nCalda = tmax[1]
nFredda = tmin[1]
indiceCalda = 1
indiceFredda = 1

for i in range(len(città)): 
    if(tmax[i] > nCalda): 
        nCalda = tmax[i]
        indiceCalda = i
    
    if(tmin[i] < nFredda): 
        nFredda = tmin[i]
        indiceFredda = i

print(f"La città più calda è {città[indiceCalda]} e la città più fredda è {città[indiceFredda]}")