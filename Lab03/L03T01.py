a = int(input("Anna ensimmäinen kokonaisluku "))
b = int(input("Anna toinen kokonaisluku "))

if a < b:
    print(f"{a} on pienempi kuin {b}")
elif a > b:
    print(f"{a} on suurempi kuin {b}")
else:
    print("Luvut ovat yhtäsuuria")