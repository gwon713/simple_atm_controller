class Account:
  def __init__(self, number):
    self.number = number
    self.money = 0

  def __str__(self):
    return f"Account : {self.number}"
  
  def deposit(self, money):
    self.money += money
    
  def withdraw(self, money):
    if self.money - money < 0:
      raise Exception('잔액이 부족합니다')
    else:
      self.money -= money