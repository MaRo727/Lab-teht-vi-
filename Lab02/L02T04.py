nimi = input("Mikä on nimesi? ")
ika = input("Milloin olet syntynyt ")
ikaNumeroitu = int(ika)
ikaLaskettu = 2023 - ikaNumeroitu
ikaTeksti = str(ikaLaskettu)
tervehdys = ("Hei " + nimi + ",")
oletvanha = ("olet " + ikaTeksti + " vuotta vanha.")
print(tervehdys, oletvanha)