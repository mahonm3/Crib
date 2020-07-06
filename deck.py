from card import Card
class Deck():
    def __init__(self):
        self.cards= []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for face in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                c=Card(suit, face)
                self.cards.append(c)
    
