tiedosto = "L09T01.txt"
with open(tiedosto, "r") as file:
    sisalto = file.read().lower()
    sanatYksitellen = sisalto.split()
    sukunimi = ", ".join(sorted(sanatYksitellen))
print(sukunimi)