lista = []
while True:
    nimi = input("Oppilaiden nimet: ")
    if nimi == "":
        break
    else:
        lista.append(nimi)
        
print("Oppilaiden määrä: ", len(lista))
print("Oppilaat:", ', '.join(lista))