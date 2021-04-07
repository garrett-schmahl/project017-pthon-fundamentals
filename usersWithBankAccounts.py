class BankAccount:
  def __init__(self, account_type, balance, interest_rate):
    self.balance = balance
    self.interest_rate = interest_rate
    self.account_type = account_type


  def deposit(self, amount):
    self.balance += amount
    return self


  def withdraw(self, amount):
    if self.balance > 0:
      self.balance -= amount
      return True
    else:
      return False


  def yield_interest(self):
    if self.balance > 0:
      self.balance += self.balance*self.interest_rate
      return True
    else:
      return False


class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.accounts = {}


  def deposit(self, amount, account_type):
    self.accounts[account_type].deposit(amount)
    print(f"Deposited {amount} into {self.name}'s {account_type} account. Current balance is ${self.accounts[account_type].balance:.2f}")
    return self


  def withdraw(self, amount, account_type):
    valid = self.accounts[account_type].withdraw(amount)
    if valid:
      print(f"Withdrew {amount} from {self.name}'s {account_type} account. Current balance is ${self.accounts[account_type].balance:.2f}")
      return self
    else:
      return errorLog()
    


  def yield_interest(self):
    for account in self.accounts:
      print(f"Balance of your {account} account is {self.accounts[account].balance:.2f}. Your account's interest rate is {self.accounts[account].interestRate*100}%")
      valid = self.accounts[account].yield_interest()
      if valid:
        print(f"The new balance of your {account} account is {self.accounts[account].balance:.2f}")
        return self
      else:
        return errorLog()
   

  def transfer_money(self, self_account_type, target, target_account_type, amount):
    valid = self.withdraw(amount, self_account_type)
    if valid:
      target.deposit(amount, target_account_type)
      print(f"Transferred {amount} from {self.name}'s {self_account_type} account, to {target.name}'s {target_account_type} account.")
      return self
    else:
      return errorLog()


  def display_account_info(self):
    print(f"Hello {self.name}")
    print(f"Your email is is {self.email}")
    if self.accounts:
      for account in self.accounts.keys():
        print(f"Your {account} balance is {self.accounts[account].balance:.2f}")
        print(f"Your {account} interest rate is {self.accounts[account].interest_rate*100}%")
    else:
      print("You don't have any accounts, you should create one, peasent.")
    return self


  def create_new_account(self, new_account_type, new_account_balance = 0, new_account_interest_rate = .01):
    self.accounts[new_account_type] = BankAccount(new_account_type, new_account_balance, new_account_interest_rate)
    return self

def errorLog():
  print("Error: User is poor ;.;")
  return False

#user initialization
kaguya = User("Kaguya Shinomiya", "kaguya@shinomiya.love")
chika = User("Chika Fujiwara", "chika@fujiwara.dance")
miyuki = User("Miyuki Shirogane", "miyuki@shirogane.pres")


kaguya.create_new_account("checking").create_new_account("saving", 0, .02)
chika.create_new_account("checking").create_new_account("saving", 0, .02)
miyuki.create_new_account("checking").create_new_account("saving", 0, .02)


#user 1 tasks
kaguya.deposit(10, "checking").deposit(5, "saving").deposit(15, "checking").withdraw(15, "checking").yield_interest().display_account_info()

#user 2 tasks
chika.deposit(5, "saving").deposit(20, "checking").withdraw(5, "saving").withdraw(10, "checking").yield_interest().display_account_info()

#user 3 tasks
miyuki.deposit(100, "checking").withdraw(10, "checking").withdraw(10, "checking").withdraw(10, "checking").yield_interest().display_account_info()

#challenge
kaguya.transfer_money("saving", miyuki, "checking", 10).display_account_info()
miyuki.display_account_info()