import unittest
from card import Card
from game import Game

class testGame(unittest.TestCase):

    def testDealTwo(self):
        game=Game(["me", "other"])
        game.deal()
        self.assertEqual(len(game.playerHand["me"]), 6)
        self.assertEqual(len(game.playerHand["other"]), 6)

    def testDealFour(self):
        game=Game(["me", "other", "teammate", "otherTeammate"])
        game.deal()
        self.assertEqual(len(game.playerHand["me"]), 5)
        self.assertEqual(len(game.playerHand["other"]), 5)
        self.assertEqual(len(game.playerHand["teammate"]), 5)
        self.assertEqual(len(game.playerHand["otherTeammate"]), 5)

    def testDiscardToKitty(self):
        game=Game(["me", "other"])
        game.deal()
        cards = game.playerHand["me"][1:3]
        game.discardToKitty("me", cards) 
        self.assertEqual(len(game.playerHand["me"]), 4)
        self.assertEqual(len(game.kitty), 2)       
