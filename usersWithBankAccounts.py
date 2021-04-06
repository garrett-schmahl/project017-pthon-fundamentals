class BankAccount:
  def __init__(self, balance = 0, interestRate = .01):
    self.balance = balance
    self.interestRate = interestRate

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.accounts = {
      "checking": BankAccount(),
      "saving": BankAccount(0, .02)
    }

  def deposit(self, amount, accountType):
    self.accounts[accountType].balance += amount
    return self

  def withdraw(self, amount, accountType):
    self.accounts[accountType].balance -= amount
    return self

  def yieldInterest(self, accountType):
    for account in self.accounts:
      if self.accounts[account].balance > 0:
        self.accounts[account].balance = self.accounts[account].balance+self.accounts[account].balance*self.accounts[account].interestRate
    return self

  def transferMoney(self, selfAccountType, target, targetAccountType, amount):
    self.withdraw(amount, selfAccountType)
    target.deposit(amount, targetAccountType)
    print(f"Transferred {amount} from {self.name}'s {selfAccountType} account, to {target.name}'s {targetAccountType} account.")
    return self

  def displayAccountInfo(self):
    print(f"Hello {self.name}")
    print(f"Your email is is {self.email}")
    for account in self.accounts.keys():
      print(f"Your {account} balance is {self.accounts[account].balance}")
      print(f"Your {account} interest rate is {self.accounts[account].interestRate}")
    return self
  
  def createNewAccount(self, newAccountName, newAccountBalance, newAccountInterestRate):
    self.accounts[newAccountName] = BankAccount(newAccountBalance, newAccountInterestRate)
    return self


kaguya = User("Kaguya", "kaguya@shinomiya.love")
chika = User("Chika", "chika@fujiwara.dance")
miyuki = User("Miyuki", "miyuki@shirogane.pres")


#user 1 tasks
kaguya.deposit(10, "checking").deposit(5, "saving").deposit(15, "checking").withdraw(15, "checking").displayAccountInfo()

#user 2 tasks
chika.deposit(5, "saving").deposit(20, "checking").withdraw(5, "saving").withdraw(10, "checking").displayAccountInfo()

#user 3 tasks
miyuki.deposit(100, "checking").withdraw(10, "checking").withdraw(10, "checking").withdraw(10, "checking").displayAccountInfo()

#challenge
kaguya.transferMoney("saving", miyuki, "checking", 10).displayAccountInfo()
miyuki.displayAccountInfo()

kaguya.createNewAccount("secret_account", 500, .05).displayAccountInfo()