print ("Questo programma calcola i crediti attribuibili a uno studente in basa all'anno scolastico.")
media = int(input("Inserire la media dei voti dello studente: "))
annoScolastico = int(input("inserire se lo studente si trova in terza(3) in quarta(4) e in quinta(5). "))

if (annoScolastico == 3):
    if (media == 6):
        print ("I crediti assegnati a questo studente sono pari a 7-8") 
    elif (6 < media <= 7):
        print ("I crediti assegnati a questo studente sono pari a 8-9") 
    elif (7 < media <= 8):
        print ("I crediti assegnati a questo studente sono pari a 9-10") 
    elif (8 < media <= 9):
        print ("I crediti assegnati a questo studente sono pari a 10-11") 
    elif (9 < media <= 10):
        print ("I crediti assegnati a questo studente sono pari a 11-12")
    else: 
        print("Valore inserito non valido") 
elif (annoScolastico == 4): 
    if (media == 6):
        print ("I crediti assegnati a questo studente sono pari a 8-9")
    elif (6 < media <= 7):
        print ("I crediti assegnati a questo studente sono pari a 9-10") 
    elif (7 < media <= 8):
        print ("I crediti assegnati a questo studente sono pari a 10-11")
    elif (8 < media <= 9):
        print ("I crediti assegnati a questo studente sono pari a 11-12") 
    elif (9 < media <= 10):
        print ("I crediti assegnati a questo studente sono pari a 12-13")
    else: 
        print("Valore inserito non valido") 
    
elif (annoScolastico == 5): 
    if (media == 6):
        print ("I crediti assegnati a questo studente sono pari a 9-10")
    elif (6 < media <= 7):
        print ("I crediti assegnati a questo studente sono pari a 10-11") 
    elif (7 < media <= 8):
        print ("I crediti assegnati a questo studente sono pari a 11-12")
    elif (8 < media <= 9):
        print ("I crediti assegnati a questo studente sono pari a 13-14") 
    elif (9 < media <= 10):
        print ("I crediti assegnati a questo studente sono pari a 14-15") 
    else: 
        print("Valore inserito non valido")
else: 
    print("Valore inserito non valido")