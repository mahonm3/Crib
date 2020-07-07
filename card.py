class Card():
    def __init__(self, suit, face):
        self.suit:str = suit
        self.face:str=face
        if self.face =="A":
            self.value = 1
            self.position = 1
        elif (self.face =="J") or (self.face =="Q") or (self.face=="K"):
            self.value = 10
        else:
            self.value = int(self.face)
            self.position = int(self.face)
            
        if (self.face == "J"):
            self.position = 11
        if (self.face == "Q"):
            self.position = 12
        if(self.face == "K"):
            self.position = 13

    def __str__(self):
        return self.face+self.suit[0]
    def __eq__(self, other):
        return self.suit==other.suit and self.face==other.face


  