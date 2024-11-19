print ("Questo programma calcola la media dei lanci di un atleta")

lancio1 = int(input("Inserire il valore del lancio n.1: "))
lancio2 = int(input("Inserire il valore del lancio n.2: "))
lancio3 = int(input("Inserire il valore del lancio n.3: "))
lancio4 = int(input("Inserire il valore del lancio n.4: "))
lancio5 = int(input("Inserire il valore del lancio n.5: "))

numeriCoivoltiMedia = 0

if (lancio1 == 0):
    numeriCoivoltiMedia = numeriCoivoltiMedia + 1
elif (lancio2 == 0):
    numeriCoivoltiMedia = numeriCoivoltiMedia + 1
elif (lancio3 == 0):
    numeriCoivoltiMedia = numeriCoivoltiMedia + 1
elif (lancio4 == 0):
    numeriCoivoltiMedia = numeriCoivoltiMedia + 1
elif (lancio5 == 0):
    numeriCoivoltiMedia = numeriCoivoltiMedia + 1

media = (lancio1 + lancio2 + lancio3 + lancio4 + lancio5)/numeriCoivoltiMedia
print = (f"La media finale è di {media}.")
