#Esercizio focalizzato sul funzionamento della condizione if



numeroAnni = int (input("Inserisci i tuoi anni \n"))

if (numeroAnni < 11):
    print("Sei un bambino")
elif(numeroAnni >= 11, numeroAnni < 18):
    print("Sei un adolescente")
else:
    print("Sei un adulto")
