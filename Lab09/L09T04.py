tiedosto = "nimet.txt"
with open(tiedosto, "r") as file:
    sisalto = file.read().lower()
    nimet = sisalto.split()
nimiSumma = len(nimet)
laskuri = {}
for nimi in nimet:
    laskuri[nimi] = laskuri.get(nimi, 0) + 1
print(f"Nimiä löytyy {nimiSumma} kappaletta")
print(laskuri)