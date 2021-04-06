class user:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
  def withdraw(self, amount):
    self.balance -= amount
    return self
  def deposit(self, amount):
    self.balance += amount
    return self
  def logBalance(self):
    print(f"User {self.name} balance is ${self.balance}")
    return self
  def transferMoney(self, other, amount):
    self.balance -= amount
    other.balance += amount
    return self


kaguya = user("Kaguya", 100)
chika = user("Chika", 5)
miyuki = user("Miyuki", 80)


print(kaguya.name)
kaguya.deposit(10).deposit(5).deposit(15).withdraw(15).logBalance()

print(chika.name)
chika.deposit(5).deposit(20).withdraw(5).withdraw(10).logBalance()

print(miyuki.name)
miyuki.deposit(100).withdraw(10).withdraw(10).withdraw(10).logBalance()

kaguya.transferMoney(miyuki, 10).logBalance()
miyuki.logBalance()