from card import Card

class HandCalculator():
    def calculateScore(self, hand, cutCard):
        rightsuit = cutCard.suit
        score=0
        if Card(rightsuit, "J") in hand:
            score+=1
        return score


