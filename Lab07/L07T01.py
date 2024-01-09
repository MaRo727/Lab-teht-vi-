import random
class Pelikortit:
    maa = ""
    arvo = ""
    def __str__(self):
        return f"{self.maa} {self.arvo}" 
    def __init__(self, maa = "", arvo = ""):
            self.maa = maa
            self.arvo = arvo
# for loopisse tehdään itse kortti viiteen kertaan, se saa random maan ja random arvon.
for i in range(5):
    korttiMaat = ["Pata", "Risti", "Ruutu", "Hertta"]
    korttiArvo = random.randrange(2, 15)
    kortti = Pelikortit(random.choice(korttiMaat), korttiArvo)
    print(kortti)

