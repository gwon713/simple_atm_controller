class Card:
  def __init__(self, number, cardPwd):
    self.number = number
    self.cardPwd = cardPwd
    self.account = []

  def addAccount(self, account):
    if len(self.findOne(account.number)) < 1:
      self.account.append(account)
    else: 
      raise Exception(f"{account.number} 계좌는 중복된 등록입니다")