num = 0
while True:
    try:
        luku = input("Anna luku: ")
        if luku == "":
            break
        num = int(luku)
    except ValueError:
        print("Luku ei oo numero")


print(num)