from deck import Deck

class Game(): 
    def __init__(self, players):
        self.deck= Deck()
        self.players=players
        self.playerScores={}
        self.playerHand={}
        self.playerPegHand={}
        for player in self.players:
            self.playerScores[player] = 0
            self.playerHand[player]=[]
            self.playerPegHand[player]=[]
        self.currentDealer=None
        self.cutCard=None

    def setDealer(self, player):
        self.dealer=player

    def deal(self):
        for player in self.players:
            if len(self.players)==2:
                for i in range(0,6):
                    self.playerHand[player].append(self.deck.drawCard())
            if len(self.players)==3 or len(self.players)==4:
                for i in range(0,5):
                    self.playerHand[player].append(self.deck.drawCard())
            


            
