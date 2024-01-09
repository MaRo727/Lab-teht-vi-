def celToFah(temp):
    fah = temp * 9/5 + 32
    return round(fah, 1)

def fahToCel(temp):
    cel = (temp - 32) * 5 / 9
    return round(cel, 1)

print(celToFah(10.0))
print(fahToCel(38.0))