class Human():
    name = ""
    age = ""
    def __str__(self):
        return f"Nimi: {self.name}, Ikä: {self.age}"
    def __init__ (self, name = "", age = ""):
        self.name = name
        self.age = age
person1 = Human("Adam", 19)
person2 = Human("Eve", 18)
print(person1)
print(person2)