
import random
# lotto tuottaa random arvon 1 ja 41 väliltä
def lotto():
    lottoNro = random.randint(1, 41)
    return str(lottoNro)
lottoNumerot = []
#looppaa 7 kertaa ja työntää siis lottofunktion random luvun listaan.
for i in range(7):
    lottoNumerot.append(lotto())
# join metodi yhdistää kaikki arvot jonoon ", " erotuksella. sorted järjestää luvut
# ja key lopussa varmistaa, että sorted metodi toimii, sillä lottoNumerot ovat string muodossa.
lottoJarjestys = ', '.join(sorted(lottoNumerot, key=int))
print(lottoJarjestys)