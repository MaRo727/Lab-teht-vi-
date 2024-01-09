kaveriLista = []
for x in range(10):
    kaveri = input("Kerro kaverin nimi ")
    if kaveri == "":
        print("Älä jätä tyhjää")
        break
    else:
        kaveriLista.append(kaveri)
print(kaveriLista)
print(kaveriLista[::-1])