class bankAccount:
  def __init__(self, balance = 0, interestRate = .01):
    self.balance = balance
    self.interestRate = interestRate
  def deposit(self, amount):
    self.balance += amount
    return self
  def withdraw(self, amount):
    self.balance -= amount
    return self
  def displayAccountInfo(self):
    print(f"Your balance is {self.balance}")
    return self
  def yieldInterest(self):
    if self.balance > 0:
      self.balance = self.balance+self.balance*self.interestRate
    return self

charles = bankAccount()
lelouch = bankAccount(100, .02)

charles.deposit(10).deposit(5).deposit(7).withdraw(15).yieldInterest().displayAccountInfo()
lelouch.deposit(10).deposit(5).withdraw(15).withdraw(10).withdraw(17).withdraw(25).yieldInterest().displayAccountInfo()