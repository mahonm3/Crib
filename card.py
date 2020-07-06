class Card():
    def __init__(self, suit, face):
        self.suit:str = suit
        self.face:str=face
        if self.face =="A":
            self.value = 1
        elif (self.face =="J") or (self.face =="Q") or (self.face=="K"):
            self.value = 10
        else:
            self.value = int(self.face)
    def __str__(self):
        return self.face+self.suit[0]

    