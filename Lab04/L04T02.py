sade1 = int(input("Anna maanantain sademäärä "))
sade2 = int(input("Anna tiistian sademäärä "))
sade3 = int(input("Anna keskiviikon sademäärä "))
sade4 = int(input("Anna torstain sademäärä "))
sade5 = int(input("Anna perjantain sademäärä "))
sade6 = int(input("Anna lauantain sademäärä "))
sade7 = int(input("Anna sunnuntain sademäärä "))
summa = 0
lista = [sade1, sade2, sade3, sade4, sade5, sade6, sade7]

for i in lista:
    summa += i

print(f"Viikon sademäärä on: {summa}")