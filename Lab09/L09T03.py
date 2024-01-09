

while True:
    luku = input("Anna kokonaisluku: ")
    if luku == "":
        break
    else:
        tiedosto = "luvut.txt"
        # Kirjoittaa käyttäjän syöttämän luvun tiedostoon ja "\n" tekee luvun aina uudelle riville.
        with open(tiedosto, "a") as file:
            file.write(luku + "\n")
# lukee tiedoston sisällön ja jakaa sen luvut muuttuujaan, 
# maara vain tairkistaa luvut muuttujan pituuden ja antaa tuloksen.
with open(tiedosto, "r") as file:
    sisalto = file.read()
    luvut = sisalto.split()
    maara = len(luvut)
print(f"Tiedostossa on {maara} lukua")
# alla oleva tyhjentää aina tiedoston operaation jälkeen, 
# jottei tarvitse manuaalisesti poistaa tiedoston sisältöä aina joka yrityksellä
with open(tiedosto, "w") as file:
    file.write("")