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
    print(f"Deposited {amount} into {self.name}'s {accountType} account. Current balance is ${self.accounts[accountType].balance:.2f}")
    return self

  def withdraw(self, amount, accountType):
    self.accounts[accountType].balance -= amount
    print(f"Withdrew {amount} from {self.name}'s {accountType} account. Current balance is ${self.accounts[accountType].balance:.2f}")
    return self

  def yieldInterest(self):
    for account in self.accounts:
      if self.accounts[account].balance > 0:
        print(f"Balance of your {account} account is {self.accounts[account].balance:.2f}. Your account's interest rate is {self.accounts[account].interestRate}")
        self.accounts[account].balance += self.accounts[account].balance*self.accounts[account].interestRate
        print(f"The new balance of your {account} account is {self.accounts[account].balance:.2f}")
      else:
        print("Error: You are poor ;.;")
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
      print(f"Your {account} balance is {self.accounts[account].balance:.2f}")
      print(f"Your {account} interest rate is {self.accounts[account].interestRate}")
    return self
  
  def createNewAccount(self, newAccountName, newAccountBalance, newAccountInterestRate):
    self.accounts[newAccountName] = BankAccount(newAccountBalance, newAccountInterestRate)
    return self


kaguya = User("Kaguya Shinomiya", "kaguya@shinomiya.love")
chika = User("Chika Fujiwara", "chika@fujiwara.dance")
miyuki = User("Miyuki Shirogane", "miyuki@shirogane.pres")


#user 1 tasks
kaguya.deposit(10, "checking").deposit(5, "saving").deposit(15, "checking").withdraw(15, "checking").yieldInterest().displayAccountInfo()

#user 2 tasks
chika.deposit(5, "saving").deposit(20, "checking").withdraw(5, "saving").withdraw(10, "checking").yieldInterest().displayAccountInfo()

#user 3 tasks
miyuki.deposit(100, "checking").withdraw(10, "checking").withdraw(10, "checking").withdraw(10, "checking").yieldInterest().displayAccountInfo()

#challenge
kaguya.transferMoney("saving", miyuki, "checking", 10).displayAccountInfo()
miyuki.displayAccountInfo()

kaguya.createNewAccount("secret_account", 500, .05).displayAccountInfo()