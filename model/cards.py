class Cards:
  def __init__(self):
    self.cards = []

  def findAll(self):
    return self.cards
  
  def findOne(self, cardNum):
    return filter(lambda card: card.number == cardNum, self.cards)
    
  def addCard(self, card):
    if len(list(self.findOne(card.number))) < 1:
      self.cards.append(card)
    else: 
      raise Exception(f"{card.number} 카드는 중복된 등록입니다")