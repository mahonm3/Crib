import unittest
from hand_calculator import HandCalculator
from card import Card


class TestHandCalculator(unittest.TestCase):
    def testRightJack(self):
        hc=HandCalculator()
        score = hc.calculateScore([Card("Hearts", "4"), Card("Spade", "J"), Card("Club", "6"), Card("Club", "7")], Card("Spade", "3"), False)
        self.assertEqual(1,score)
    def testZeroHand(self):
        hc=HandCalculator()
        score = hc.calculateScore([Card("Hearts", "4"), Card("Spade", "J"), Card("Club", "6"), Card("Club", "7")], Card("Heart", "3"), False)
        self.assertEqual(0,score)
    def testFlushHandWithCut(self):
        hc = HandCalculator()
        score = hc.calculateScore(
            [Card("Hearts", "2"), Card("Hearts", "4"), Card("Hearts", "6"), Card("Hearts", "8")],
            Card("Hearts", "10"), False
        )
        self.assertEqual(5,score)
    def testFlushHandWithOutCut(self):
        hc = HandCalculator()
        score = hc.calculateScore(
            [Card("Hearts", "2"), Card("Hearts", "4"), Card("Hearts", "6"), Card("Hearts", "8")],
            Card("Club", "10"), False
        )
        self.assertEqual(4,score)   

    def testFlushHandZero(self):
        hc = HandCalculator()
        score = hc.calculateScore(
            [Card("Hearts", "2"), Card("Club", "4"), Card("Hearts", "6"), Card("Hearts", "8")],
            Card("Hearts", "10"), False
        )
        self.assertEqual(0,score)         

    def testFlushKittyWithCut(self):
        hc = HandCalculator()
        score = hc.calculateScore(
            [Card("Hearts", "2"), Card("Hearts", "4"), Card("Hearts", "6"), Card("Hearts", "8")],
            Card("Hearts", "10"), True
        )
        self.assertEqual(5,score)

    def testFlushKittyWithOutCut(self):
        hc = HandCalculator()
        score = hc.calculateScore(
            [Card("Hearts", "2"), Card("Hearts", "4"), Card("Hearts", "6"), Card("Hearts", "8")],
            Card("Club", "10"), True
        )
        self.assertEqual(0,score)   
    def testFlushKittyZero(self):
        hc = HandCalculator()
        score = hc.calculateScore(
            [Card("Hearts", "2"), Card("Club", "4"), Card("Hearts", "6"), Card("Hearts", "8")],
            Card("Hearts", "10"), True
        )
        self.assertEqual(0,score)   

    def testFindRunsZero(self):
        hcr = HandCalculator()
        score = hcr.calculateRunScore(
            [Card("Hearts", "2"), Card("Club", "4"), Card("Hearts", "6"), Card("Spade", "8"),
            Card("Hearts", "10")])
        self.assertEqual(0, score)

    def testFindRunsZeroTwoAdjacent(self):
        hcr = HandCalculator()
        score = hcr.calculateRunScore(
            [Card("Hearts", "2"), Card("Club", "A"), Card("Hearts", "Q"), Card("Spade", "8"),
            Card("Hearts", "10")])
        self.assertEqual(0, score)

    def testFindRunsThree(self):
         hcr = HandCalculator()
         score = hcr.calculateRunScore(
            [Card("Hearts", "2"), Card("Club", "4"), Card("Hearts", "3"), Card("Spade", "8"),
            Card("Hearts", "10")])
         self.assertEqual(3, score)       
        



    def testRunofFour(self):
        hcr = HandCalculator()
        score= hcr.calculateRunScore([Card("Hearts", "A"), Card("Club", "2"), Card("Spade", "4"), Card("Diamond","3"),
         Card("Club", "8")]
         )
        self.assertEqual(4, score)

    def testRunofFive(self):
        hcr = HandCalculator()
        score= hcr.calculateRunScore([Card("Hearts", "A"), Card("Club", "2"), Card("Spade", "5"), Card("Diamond","3"),
         Card("Club", "4")]
         )
        self.assertEqual(5, score)

    def testDoubleRun(self):
        hcr = HandCalculator()
        score= hcr.calculateRunScore([Card("Hearts", "A"), Card("Club", "2"), Card("Spade", "A"), Card("Diamond","3"),
         Card("Club", "7")]
         )
        self.assertEqual(6, score)
        
    def testTripleRun(self):
        hcr = HandCalculator()
        score= hcr.calculateRunScore([Card("Hearts", "A"), Card("Club", "2"), Card("Spade", "A"), Card("Diamond","3"),
         Card("Club", "A")]
         )
        self.assertEqual(9, score)    

    def testDoubleDoubleRun(self):
        hcr = HandCalculator()
        score= hcr.calculateRunScore([Card("Hearts", "A"), Card("Club", "2"), Card("Spade", "A"), Card("Diamond","3"),
         Card("Club", "3")]
         )
        self.assertEqual(12, score)   

    def testPair(self):
        hc = HandCalculator()
        score=hc.calculatePairScore([Card("Hearts", "A"), Card("Club", "2"), Card("Spade", "A"), Card("Diamond","3"),
         Card("Club", "4")]
         )
        self.assertEqual(2, score)

    def testTwoPair(self):
        hc = HandCalculator()
        score=hc.calculatePairScore([Card("Hearts", "A"), Card("Club", "2"), Card("Spade", "A"), Card("Diamond","3"),
         Card("Club", "2")]
         )
        self.assertEqual(4, score)

    def testThreeOfAKind(self):
        hc = HandCalculator()
        score=hc.calculatePairScore([Card("Hearts", "A"), Card("Club", "2"), Card("Spade", "A"), Card("Diamond","3"),
         Card("Club", "A")]
         )
        self.assertEqual(6, score)

    def testFourOfAKind(self):
        hc = HandCalculator()
        score=hc.calculatePairScore([Card("Hearts", "A"), Card("Club", "2"), Card("Spade", "A"), Card("Diamond","A"),
         Card("Club", "A")]
         )
        self.assertEqual(12, score)
        
    



if __name__ == "__main__":
    unittest.main() 