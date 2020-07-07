from card import Card

class HandCalculator():
    def calculateScore(self, hand, cutCard):
        score=0

        rightsuit = cutCard.suit
        if Card(rightsuit, "J") in hand:
            score+=1

        isHandFlush = True
        for card in hand:
            if hand[0].suit == card.suit:
                pass
            else: 
                isHandFlush = False 
                break
        if isHandFlush == True:
            score += 4
            if cutCard.suit == hand[0].suit:
                score +=1
        

        return score


