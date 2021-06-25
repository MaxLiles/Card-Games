import random
class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
         suits = ['hearts', 'spades', 'clubs', 'diamonds']
         values = ['Ace', '2', '3','4','5','6','7','8','9','10','Jack','Queen','King',]        
         self.cards = [Card(value,suit) for value in values for suit in suits]
         self.shuffle()
    def __str__(self):
        pass
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, num=5):
        hand = []
        for i in range(0,num):
            hand.append(self.cards.pop())
        return hand

done = False
counter = 0
while not done:
    counter +=1
    print(f"attmept #{counter}")
    deck = Deck()
    hand = deck.deal()



    if hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit:
        #done = True
        if hand[0].value == 'King' or hand[1].value == 'King' or hand[2].value == 'King' or hand[3].value == 'King' or hand[4].value =='King':
            if hand[0].value == 'Queen' or hand[1].value == 'Queen' or hand[2].value == 'Queen' or hand[3].value == 'Queen' or hand[4].value =='Queen':
                if hand[0].value == 'Ace' or hand[1].value == 'Ace' or hand[2].value == 'Ace' or hand[3].value == 'Ace' or hand[4].value =='Ace':
                    if hand[0].value == 'Jack' or hand[1].value == 'Jack' or hand[2].value == 'Jack' or hand[3].value == 'Jack' or hand[4].value =='Jack':
                        if hand[0].value == '10' or hand[1].value == '10' or hand[2].value == '10' or hand[3].value == '10' or hand[4].value =='10':
                            done = True


