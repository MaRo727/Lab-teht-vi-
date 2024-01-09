class Mobile():
    brand = ""
    model = ""
    price = 0
    def __str__(self):
        return f"{self.brand} {self.model}, {self.price} €"
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price
phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)
print(phone1)
print(phone2)