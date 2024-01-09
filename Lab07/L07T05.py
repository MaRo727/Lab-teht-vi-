class Car():
    brand = ""
    model = ""
    price = 0
    def __str__(self):
        return f"{self.brand} {self.model}, {self.price} €"
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price
autot = [   
        Car("Skoda", "Octavia", 3000), 
        Car("Audi", "A4", 4000), 
        Car("Volvo", "V70", 5000)
        ]
for yksiAuto in autot:
    print(yksiAuto)
    
summa = sum(auto.price for auto in autot)
print(f"Autojen yhteishinta: {summa} €")
