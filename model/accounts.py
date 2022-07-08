class Accounts:
  def __init__(self):
    self.accounts = []

  def findAll(self):
    return self.accounts
  
  def findOne(self, accountNum):
    return filter(lambda account: account.number == accountNum, self.accounts)
    
  def addAccount(self, account):
    if len(list(self.findOne(account.number))) < 1:
      self.accounts.append(account)
    else: 
      raise Exception(f"{account.number} 계좌는 중복된 등록입니다")