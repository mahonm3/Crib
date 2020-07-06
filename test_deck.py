import unittest
from deck import Deck

class TestDeckClass(unittest.TestCase):
    def test_create_deck(self):
        d=Deck()
        self.assertEqual(52, len(d.cards))
    def test_cards_in_suit(self):
        d= Deck()
        suitcounts = {"Hearts":0,"Diamonds":0, "Clubs":0, "Spades":0}
        for card in d.cards:
            suitcounts[card.suit]+=1
        self.assertEqual(13, suitcounts["Hearts"])
        self.assertEqual(13, suitcounts["Diamonds"])
        self.assertEqual(13, suitcounts["Clubs"])
        self.assertEqual(13, suitcounts["Spades"])

if __name__ == "__main__":
    unittest.main()