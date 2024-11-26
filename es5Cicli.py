#Esercizio focalizzato sulla funzione delle iterazioni
# Ne possiamo contare quella While e quella For

#Ciclo While, affinché
#Esercizio che conta i caratteri nella stringa finché essa non è finita
#Passando una stringa in input come parametro

stringaInput = input("Digita qui una stringa :) \n")
counter = 0
while counter !=  len(stringaInput)-1:
    counter+= 1
print ("La tua stringa ha un massimo di ", counter, "in totale")

#Ciclo For, Imperativo

Array = ['cane', 'cosa', 'pane', 'mela', 'Stereotipo', "canto", "ululato", "secco"]

for cosa in Array:
    if len(cosa) > 5:
        print("Troppo Grande oh")
    else:
        print(cosa)
