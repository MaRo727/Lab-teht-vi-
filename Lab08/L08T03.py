arvosanaLista = []
while True:
    try:
        luku = int(input("Arvosanasi (1-5): "))
        if luku < 1 or luku > 5 or "":
            break
        else:
            arvosanaLista.append(luku)
            print(arvosanaLista)
    except ValueError:
        break

arvosanaMaara = len(arvosanaLista)
arvosanaSumma = sum(arvosanaLista)
keskiarvo = arvosanaSumma / arvosanaMaara
print(f"Arvosanojesi keskiarvo on {keskiarvo}")
