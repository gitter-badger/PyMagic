import classCards
import random

class player(object):
    hand = []
    deck = []
    field = []
    grave = []
    lands = []
    health = 0
    mana = 0
    def __init__(self):
        self.InitDeck()
        self.health = 20
        for i in range(1, 8):
            self.draw()
    
    def InitDeck(self):
        for i in range(1, 61):
            self.deck.append(classCards.allCards[random.randrange(len(classCards.allCards))])
                

    def draw(self):
        self.hand.append(self.deck[(len(self.deck) - 1)])
        del self.deck[len(self.deck) - 1]

    def CanSummon(self, target):
        if target in self.hand and target.cost <= self.mana:
            return True
        else:
            return False

    def Summon(self, target):
        if self.CanSummon(target) == True:
            self.field.append(target)
            del self.hand[target]
            self.mana -= target.cost
            print(self + " summons a " + target.name + "!")

    def SeeHand(self):
        for card in self.hand:
            print(card)

    def SeeField(self):
        for card in self.field:
            print(card)

    def SeeGrave(self):
        for card in self.grave:
            print(card)

    def SeeLand(self):
        for card in self.lands:
            print(card)

    def StartTurn(self):
        if len(self.hand) < 8:
            self.draw()
        for i in self.lands:
            self.mana += i.mana
  
    def EndTurn(self):
        for m in self.field:
            m.health = m.defence
            m.untap()
