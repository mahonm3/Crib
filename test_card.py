from card import Card

import unittest
class TestCardClass(unittest.TestCase):
    def test_4ofHeartsVal(self):
        c1 = Card("Heart", "4")
        self.assertEqual(4, c1.value)
    def test_KofSpadesVal(self):
        c2= Card("Spades", "K")
        self.assertEqual(10, c2.value)
    def test_AofClubsVal(self):
        c3=Card("Clubs", "A")
        self.assertEqual(1, c3.value)
    def test_4ofHeartsPos(self):
        c1 = Card("Heart", "4")
        self.assertEqual(4, c1.position)
    def test_KofSpadesPos(self):
        c2= Card("Spades", "K")
        self.assertEqual(13, c2.position)
    def test_AofClubsPos(self):
        c3=Card("Clubs", "A")
        self.assertEqual(1, c3.position)

if __name__ == "__main__":
    unittest.main()

