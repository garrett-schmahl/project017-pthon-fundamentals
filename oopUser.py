class user:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
  def withdraw(self, amount):
    self.balance -= amount
  def deposit(self, amount):
    self.balance += amount
  def logBalance(self):
    print(f"User {self.name} balance is ${self.balance}")
  def transferMoney(self, other, amount):
    self.balance -= amount
    other.balance += amount


kaguya = user("Kaguya", 100)
chika = user("Chika", 5)
miyuki = user("Miyuki", 80)


print(kaguya.name)
kaguya.deposit(10)
kaguya.deposit(5)
kaguya.deposit(15)
kaguya.withdraw(15)
kaguya.logBalance()

print(chika.name)
chika.deposit(5)
chika.deposit(20)
chika.withdraw(5)
chika.withdraw(10)
chika.logBalance()

print(miyuki.name)
miyuki.deposit(100)
miyuki.withdraw(10)
miyuki.withdraw(10)
miyuki.withdraw(10)
miyuki.logBalance()

kaguya.transferMoney(miyuki, 10)
kaguya.logBalance()
miyuki.logBalance()