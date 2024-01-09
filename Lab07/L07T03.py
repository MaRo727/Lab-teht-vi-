class Cat():
    name = ""
    color = ""
    def __str__(self):
        return f"{self.name}, Color: {self.color}"
    def __init__(self, name = "", color = ""):
        self.name = name
        self.color = color
    def miau(self):
        return "Meoooooow!"
kissa1 = Cat("Kit", "Black")
kissa2 = Cat("Kat", "White")
print(kissa1)
print(kissa2)
print(f"{kissa1.name} says: {kissa1.miau()}")
print(f"{kissa2.name} says: {kissa2.miau()}")
