import unittest
from hand_calculator import HandCalculator
from card import Card


class TestHandCalculator(unittest.TestCase):
    def testRightJack(self):
        hc=HandCalculator()
        score = hc.calculateScore([Card("Hearts", "4"), Card("Spade", "J"), Card("Club", "6"), Card("Club", "7")], Card("Spade", "3"))
        self.assertEqual(1,score)
    def testZeroHand(self):
        hc=HandCalculator()
        score = hc.calculateScore([Card("Hearts", "4"), Card("Spade", "J"), Card("Club", "6"), Card("Club", "7")], Card("Heart", "3"))
        self.assertEqual(0,score)
    def testFlushHandWithCut(self):
        hc = HandCalculator()
        score = hc.calculateScore(
            [Card("Hearts", "2"), Card("Hearts", "4"), Card("Hearts", "6"), Card("Hearts", "8")],
            Card("Hearts", "10")
        )
        self.assertEqual(5,score)
    def testFlushHandWithOutCut(self):
        hc = HandCalculator()
        score = hc.calculateScore(
            [Card("Hearts", "2"), Card("Hearts", "4"), Card("Hearts", "6"), Card("Hearts", "8")],
            Card("Club", "10")
        )
        self.assertEqual(4,score)   
    def testFlushHandZero(self):
        hc = HandCalculator()
        score = hc.calculateScore(
            [Card("Hearts", "2"), Card("Spade", "4"), Card("Hearts", "6"), Card("Hearts", "8")],
            Card("Hearts", "10")
        )
        self.assertEqual(0,score)         
            
if __name__ == "__main__":
    unittest.main() 