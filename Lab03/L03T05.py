luku_1 = int(input("Anna luku "))
luku_2 = int(input("Anna toinen luku "))
luku_3 = int(input("Anna kolmas luku "))
luku_4 = int(input("Anna neljäs luku "))
luku_5 = int(input("Anna viides luku "))
summa = 0    

lista = [luku_1, luku_2, luku_3, luku_4, luku_5]
for i in lista:
    if i > 0:
        summa += i

print(summa)