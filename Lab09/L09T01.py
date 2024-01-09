

while True:
    sukunimi = input("Anna sukunimi: ")
    if sukunimi == "":
        break
    else:
        tiedosto = "L09T01.txt"
        with open(tiedosto, "a") as file:
            file.write(sukunimi + "\n")
            file.flush()
    