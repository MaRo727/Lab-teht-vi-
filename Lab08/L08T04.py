import random
autot = {}
kirjaimet = 'ABCDEFGHIJKLMNOPRSTUVYZ'
# randomRekisteri palauttaa koko rekisterikilven, jota käytetään avaimena autot kokoelmassa.
def randomRekisteri():
    # alku ja loppu osa ovat siis kirjain osuus ja numero osuus rekisterikilvestä.
    alkuOsa = ''.join(random.choices(kirjaimet, k=3))
    loppuOsa = random.randint(1, 999)
    return f'{alkuOsa}-{loppuOsa:03d}'
autoMerkkiLista = ["Toyota", "Volkswagen", "Hyundai", "Ford", "Honda", "Nissan", "BMW", "Mercedes"]
# randomAutoMerkki funktio palauttaa yllä olevasta listasta random auton merkin
def randomAutoMerkki():
    return random.choice(autoMerkkiLista)
# for looppi pyöräyttää äkkiä 10 random rekisterikilpeä ja asettaa ne autot kokoelmaan
# Tekee hakee randomRekisteristä arvoa ja samalla asettaa sen avain arvoksi
for i in range(10):
    autot[randomRekisteri()] = randomAutoMerkki()
autotJarjestys = dict(sorted(autot.items()))
# Järjestää rekkarin perusteella kokoelman sisällä olevat arvot aakkosjärjestykseen 
for rekisterinumero, automerkki in autotJarjestys.items():
    print(f"{rekisterinumero} {automerkki}")