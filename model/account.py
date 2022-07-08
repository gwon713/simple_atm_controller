class Account:
  def __init__(self, number, balance=0, cardNum=None):
    self.cardNum = cardNum
    self.number = number
    self.balance = balance

  def __str__(self):
    return f"Account : {self.number}, balance: ${self.balance}, cardNum: {self.cardNum}"
  
  def deposit(self, amount):
    self.balance += amount
    return True
    
  def withdraw(self, amount):
    if self.balance - amount < 0:
      print(f"!!!Lack of balance // Balance: ${self.balance}!!!")
      return False
    else:
      self.balance -= amount
      return True