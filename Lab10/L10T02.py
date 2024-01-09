import datetime
vuosi = int(input("Instert year "))
karkausvuosi = 4
nykyVuosi = datetime.date.today().year
while True:
    karkausvuosi += 4
    if karkausvuosi == vuosi:
        print(f"{vuosi} is a leap year!")
        break
    elif karkausvuosi > 999999:
        print(f"{vuosi} is not a leap year!")
        break