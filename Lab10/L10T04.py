file = open("names.txt", "r", encoding='utf-8')
rivi = file.readlines()

pisinNimi = ""
edellinenNimi, nykyinenNimi = -1, -1
for nimi in rivi:
    nykyinenNimi = len(nimi)
    if nykyinenNimi > edellinenNimi:
        pisinNimi = nimi
    edellinenNimi = nykyinenNimi
    
print(pisinNimi)