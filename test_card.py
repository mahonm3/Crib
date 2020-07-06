from card import Card

import unittest
class TestCardClass(unittest.TestCase):
    def test_4ofHearts(self):
        c1 = Card("Heart", "4")
        self.assertEqual(4, c1.value)
    def test_KofSpades(self):
        c2= Card("Spades", "K")
        self.assertEqual(10, c2.value)
    def test_AofClubs(self):
        c3=Card("Clubs", "A")
        self.assertEqual(1, c3.value)

if __name__ == "__main__":
    unittest.main()

