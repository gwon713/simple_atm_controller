from model.account import *
from model.cards import *
from model.card import *

# Card Register
account1 = Account("111-1111111-111")
account2 = Account("222-2222222-222")
account3 = Account("333-3333333-333")
account4 = Account("444-4444444-444")

card1 = Card("1111-1111-1111-1111", "1234")

# card1.addAccount(account1)
# card1.addAccount(account2)

card2 = Card("2222-2222-2222-2222", "1234")

card2.addAccount(account3)
card2.addAccount(account4)

global cards 
cards = Cards()

cards.addCard(card1)
cards.addCard(card2)

for card in cards.findAll():
  print(str(card))

def insertCard():
  print("Welcome ATM")
  cardNum=str(input("카드를 넣어주세요: "))

  card = list(cards.findOne(cardNum))

  if not len(card):
    print("등록되지 않은 카드입니다")
    insertCard()
  else:
    if card[0].stop == True:
      print(f"{card[0].number} 카드는 정지된 상태입니다")
      insertCard()
    if validateCardPIN(card[0]) == True:
      return card[0]
    else:
      insertCard()
  
def validateCardPIN(targerCard):
  pinNum=str(input("Enter your 4 digit PIN Number : "))

  if targerCard.validatePIN(pinNum) == True:
    print("인증되었습니다")
    return selectAccount(targerCard)
  else:
    if targerCard.pinErrorCnt > 2:
      targerCard.stopCard()
      print(f"{targerCard.number} 카드 정지")
      return insertCard()
    validateCardPIN(targerCard)

def selectAccount(targerCard):
  print(f"Card {targerCard.number} Account List")
  accounts = targerCard.findAllAccount()
  if not len(list(accounts)) > 0:
    print("거래를 진행할 계좌가 없습니다. 메인화면으로 돌아갑니다")
    insertCard()
  for idx, account in enumerate(accounts):
    print(f"{idx}. {account}")
  accountNum=int(input("Select your Account: "))

def ATM():
  insertCard()
  
ATM()