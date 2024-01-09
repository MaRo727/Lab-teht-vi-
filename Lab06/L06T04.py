import random
lista = []
# Toistaa viisi kertaa for loopin, tekee random numeron 1-20 ja työntää sen listaan.
for i in range(5):
    tuomari = int(random.randrange(1, 20))
    lista.append(tuomari)
print(f"Kaikki 5 arvosanaa: {lista}")
lista.remove(max(lista))
lista.remove(min(lista))
print(f"Pienin ja suurin arvosana poistettu: {lista}")
tulos = sum(lista)
print(f"Loppusumma: {tulos}")
