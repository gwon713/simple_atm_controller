from model.account import *
from model.accounts import *
from model.card import *
from model.cards import *

global cards, accounts 
cards = Cards()
accounts = Accounts()
# Card Register
card1 = Card("1111-1111-1111-1111", "1234")

account1 = Account("111-1111111-111", 10000, card1.number)
card1.addAccount(account1)

card2 = Card("2222-2222-2222-2222", "5678")

account2 = Account("222-2222222-222", 0, card2.number)
card2.addAccount(account2)
account3 = Account("333-3333333-333", 200, card2.number)
card2.addAccount(account3)

card3 = Card("3333-3333-3333-3333", "1111")

account4 = Account("444-4444444-444", 1)
account5 = Account("555-5555555-555", 500)

# Add Card List
cards.addCard(card1)
cards.addCard(card2)
cards.addCard(card3)

# Add Account List
accounts.addAccount(account1)
accounts.addAccount(account2)
accounts.addAccount(account3)
accounts.addAccount(account4)
accounts.addAccount(account5)

def printDividingLine():
  print("------------------------------")

def printServiceList():
  print("Service List")
  print("0. Return to the Main Screen")
  print("1. See Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Return to the Select Account")

def printAllInfo():
  for card in cards.findAll():
    print(" ======== Card Info ========")
    print(str(card))

  print(" ======== Account Info ========")
  for account in accounts.findAll():
    print(str(account))

def printCardAccounts(targerCard, cardAccounts):
  print(f"Card {targerCard.number} Account List")
  for idx, account in enumerate(cardAccounts):
    print(f"{idx+1}. Account: {account.number}")

def insertCard():
  printDividingLine()
  cardNum=str(input("Please insert your card: ")).strip()

  card = list(cards.findOne(cardNum))

  if not len(card):
    print("!!!This card is not registered!!!")
    return insertCard()
  else:
    if card[0].stopped == True:
      print(f"!!!Card {card[0].number} is suspended!!!")
      return insertCard()
    return validateCardPIN(card[0])
  
def validateCardPIN(targerCard):
  printDividingLine()
  pinNum=str(input("Enter your 4 digit PIN Number : ")).strip()

  if not len(pinNum) == 4:
    print("!!!Please enter only 4 digits!!!")
    return validateCardPIN(targerCard)

  if targerCard.validatePIN(pinNum) == True:
    print("Validation successful")
    return selectAccount(targerCard)
  else:
    if targerCard.pinErrorCnt > 2:
      targerCard.stopCard()
      print(f"!!!Suspend the card {targerCard.number}!!!")
      return insertCard()
    return validateCardPIN(targerCard)

def selectAccount(targerCard):
  printDividingLine()
  accounts = targerCard.findAllAccount()
  if not len(list(accounts)) > 0:
    print("!!!There are no accounts to trade. Return to the main screen!!!")
    return ATM()

  printCardAccounts(targerCard, accounts)

  accountNum=int(input("Select your Account: "))

  if 0 < accountNum <= len(list(accounts)) :
    account = list(accounts)[accountNum-1]
    print(account)
    return selectService(targerCard, account)
  else: 
    print("!!!Wrong Select Account!!!")
    return selectAccount(targerCard)

def selectService(targerCard, targerAccount):
  printDividingLine()
  printServiceList()

  serviceNum=int(input("Select your Account: "))

  match serviceNum:
    case 0:
      return ATM()
    case 1:
      return seeBalanceAccount(targerCard, targerAccount)
    case 2:
      return depositAccount(targerCard, targerAccount)
    case 3:
      return withdrawAccount(targerCard, targerAccount)
    case 4:
      return selectAccount(targerCard)
    case _:
      print("!!!Wrong Select Service!!!")
      return selectService(targerCard, targerAccount)

def seeBalanceAccount(targerCard, targerAccount):
  printDividingLine()
  targerAccount.seeBalance()
  return selectService(targerCard, targerAccount)

def depositAccount(targerCard, targerAccount):
  printDividingLine()
  depositAmount=int(float(input("Enter the deposit amount: $")))
  if targerAccount.deposit(depositAmount) == True:
    print("Deposit successful")
    targerAccount.seeBalance()
    return selectService(targerCard, targerAccount)
  else:
    print("!!!Deposit failed!!!")
    return depositAccount(targerCard, targerAccount)

def withdrawAccount(targerCard, targerAccount):
  printDividingLine()
  withdrawAmount=int(float(input("Enter the withdraw amount: $")))
  if targerAccount.withdraw(withdrawAmount) == True:
    print("Withdraw successful")
    targerAccount.seeBalance()
    return selectService(targerCard, targerAccount)
  else:
    print("!!!Withdraw failed!!!")
    return withdrawAccount(targerCard, targerAccount)

def ATM():
  print("==============================")
  print("======Welcome Simple ATM======")
  print("==============================")
  insertCard()

printAllInfo()
ATM()