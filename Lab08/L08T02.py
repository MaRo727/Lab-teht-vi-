
rekisteriLista = []
while True:
    rekkari = input("Anna rekisterikilpi: ")
    rekisteriLista.append(rekkari.lower())
    print(rekisteriLista)
    if rekkari == "":
        break

rekisteriListaSorted = sorted(rekisteriLista)
print(rekisteriListaSorted)