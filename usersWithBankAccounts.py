class bankAccount:
  def __init__(self, balance, interestRate, accountType):
    self.accountType = accountType
    self.balance = balance
    self.interestRate = interestRate

class user:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.accountSaving = bankAccount(balance=0, interestRate=0.02, accountType ="savings")
    self.accountChecking = bankAccount(balance=0, interestRate=0.01, accountType ="checking")
  def deposit(self, amount, accountType):
    if accountType == "checking":
      self.accountChecking.balance += amount
    elif accountType == "saving":
      self.accountSaving.balance += amount
    return self
  def withdraw(self, amount, accountType):
    if accountType == "checking":
      self.accountChecking.balance -= amount
    elif accountType == "saving":
      self.accountSaving.balance -= amount
    return self
  def displayAccountInfo(self):
    print(f"Hello {self.name}")
    print(f"Your email is is {self.email}")
    print(f"Your checking balance is {self.accountChecking.balance}")
    print(f"Your checking interest rate is {self.accountChecking.interestRate}")
    print(f"Your savings balance is {self.accountSaving.balance}")
    print(f"Your savings interest rate is {self.accountSaving.interestRate}")
    return self
  def yieldInterest(self):
    if self.accountChecking.balance > 0:
      self.accountChecking.balance = self.accountChecking.balance+self.accountChecking.balance*self.accountChecking.interestRate
    if self.accountSaving.balance > 0:
      self.accountSaving.balance = self.accountSaving.balance+self.accountSaving.balance*self.accountSaving.interestRate
    return self
  def transferMoney(self, other, amount):
    self.accountChecking.balance -= amount
    other.accountChecking.balance += amount
    return self



kaguya = user("Kaguya", "kaguya@shinomiya.love")
chika = user("Chika", "chika@fujiwara.dance")
miyuki = user("Miyuki", "miyuki@shirogane.pres")


print(kaguya.name)
kaguya.deposit(10, "checking").deposit(5, "saving").deposit(15, "checking").withdraw(15, "checking").displayAccountInfo()

print(chika.name)
chika.deposit(5, "saving").deposit(20, "checking").withdraw(5, "saving").withdraw(10, "checking").displayAccountInfo()

print(miyuki.name)
miyuki.deposit(100, "checking").withdraw(10, "checking").withdraw(10, "checking").withdraw(10, "checking").displayAccountInfo()

kaguya.transferMoney(miyuki, 10).displayAccountInfo()
miyuki.displayAccountInfo()