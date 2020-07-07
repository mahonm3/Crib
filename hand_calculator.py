from card import Card

class HandCalculator():
    def calculateScore(self, hand, cutCard, isKitty):
        score=0

        rightsuit = cutCard.suit
        if Card(rightsuit, "J") in hand:
            score+=1

        if isKitty == False:
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
        
        if isKitty == True:
            isHandFlush = True
            if hand[0].suit != cutCard.suit:
                isHandFlush = False
            for card in hand:
                if hand[0].suit == card.suit:
                    pass
                else: 
                    isHandFlush = False
                    break

            if isHandFlush == True:
                score += 5

            
        

        return score


