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

        score+=self.calculateRunScore([*hand, cutCard])
        score+=self.calculatePairScore([*hand, cutCard])
        score+=self.calculateFifteensScore([*hand, cutCard])
                   
        

        return score

    def getPositionCounts(self, cards):
        countByPosition = {}
        for card in cards:
            if card.position in countByPosition:
                countByPosition[card.position] +=1
            else:
                countByPosition[card.position] = 1
        return countByPosition




    def calculateRunScore(self, cards):
        runScore = 0
        countsByPosition = self.getPositionCounts(cards)
        sortedPositions = sorted(countsByPosition)

        currentRunStart=0
        lengthOfRun = 0
        for i in range(0,len(sortedPositions)):
            lengthOfRun +=1
            if i<len(sortedPositions)-1 and sortedPositions[i+1] != 1+sortedPositions[i]:
                if lengthOfRun >2:
                    break
                else:
                    lengthOfRun = 0                
                    currentRunStart +=1
                continue
        if lengthOfRun>2:
            runScore=lengthOfRun
            for i in range(currentRunStart, (currentRunStart+lengthOfRun)):
                 runScore=runScore*countsByPosition[sortedPositions[i]]
                

        return runScore

    def calculatePairScore(self, cards):
        pairScore = 0
        countsByPosition = self.getPositionCounts(cards)
        sortedPositions = sorted(countsByPosition)
        
        for i in range(0,len(sortedPositions)):
            if countsByPosition[sortedPositions[i]]==2:
                pairScore+=2
            if countsByPosition[sortedPositions[i]]==3:
                pairScore+=6
            if countsByPosition[sortedPositions[i]]==4:
                pairScore+=12
        return pairScore

    def calculateFifteensScore(self, cards, currentSum=0, currentScore=0, indent=""):
        sortedCards=sorted(cards, key=lambda x: x.value, reverse=True)
        for i in range(0,len(sortedCards)):
            card=sortedCards[i]
            #print(indent+" current score: "+str(currentScore)+", current sum: "+str(currentSum)+ ", current card: "+str(card))
            if card.value+currentSum==15:
                currentScore+=2
                
            elif card.value+currentSum>15:
                continue
            else:
                if (i+1)<len(sortedCards):
                    nextScore=self.calculateFifteensScore(sortedCards[i+1:len(sortedCards)], (card.value+currentSum), 0, indent+"   ")
                    currentScore += nextScore
        return currentScore

    



            
                

            



