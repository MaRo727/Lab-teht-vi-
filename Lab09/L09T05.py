import random
# lotto funktio vain palauttaa random numeron 1 ja 40 väliltä
def lotto():     
    return str(random.randint(1, 40))
# rivienMäärä kysyy käyttäjältä montako lottoriviä tehdään.
rivienMaara = int(input("Montako lottoriviä pyöräytetään? "))
tiedosto = "lotto.txt"
# kirjoittaa tiedostoon ei mitään, jotta tiedosto tyhjenee aina ennen arvontaa.
with open(tiedosto, "w") as file:
    file.write("")
# looppaa koko loopin niin monta kertaa kun käyttäjä haluaa.
for i in range(rivienMaara):
    lottoRiviSet = set()
    #tallentaa lottorivi settiin 7 numeroa ja set() funktio varmistaa, että jokainen numero in uniikki.
    while len(lottoRiviSet) < 7:   
        lottoRiviSet.add(lotto())
        #lottoRivi yhdistää arrayn stringiksi ja järjestää luvut suuruusjärjestykseen
    with open(tiedosto, "a") as file:
        lottoRivi = " ".join(sorted(lottoRiviSet, key = int))   
        file.write(lottoRivi + "\n")