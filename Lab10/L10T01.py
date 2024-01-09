import datetime
tamanHetkinenVuosi = datetime.date.today().year
kayttajanSyntyma = int(input("Minä vuonna olet syntynyt? "))

kayttajanIka = tamanHetkinenVuosi - kayttajanSyntyma
if kayttajanIka < 1:
    print("baby")
elif kayttajanIka < 13:
    print("child")
elif kayttajanIka >= 13 and kayttajanIka < 20:
    print("teen")
elif kayttajanIka >= 20 and kayttajanIka < 66:
    print("adult")
else:
    print("senior")