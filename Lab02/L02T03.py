kokonimi = input("Mikä on kokonimesi? ")
valilyonti = kokonimi.find(" ")
kirjainYht = len(kokonimi)
etuLeikkaus = slice(0, valilyonti)
sukuLeikkaus = slice(valilyonti + 1, kirjainYht)

print("Etunimesi on: ", kokonimi[etuLeikkaus])
print("Sukunimesi on: ", kokonimi[sukuLeikkaus])

# Jälkikäteen miettii niin sukuleikkaus ei ole kovin hieno nimi