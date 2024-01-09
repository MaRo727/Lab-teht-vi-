class Account():
    saldo = 0
    def __str__(self):
        return f"{self.saldo}€"
    def __init__(self, saldo):
        self.saldo = saldo
    def deposit(self, amount):
        self.saldo += amount
        return self.saldo
    def withdraw(self, amount):
        if amount <= self.saldo:
            self.saldo -= amount
            return self.saldo
        else:
            print(f"Sorry you only have {pankkitili}, the withdraw cannot be done. ")
            return self.saldo
pankkitili = Account(2000)
print("Bank account created")
print(f"Bank account balance: {pankkitili}")

print("How many euros will be deposited? (120)")
pankkitili.deposit(120)
print(f"Bank account balance: {pankkitili}")

print("How many euros will be withdrawn? (1500)")
pankkitili.withdraw(1500)
print(f"Bank account balance: {pankkitili}")

print("How many euros will be withdrawn? (1500)")
pankkitili.withdraw(1500)