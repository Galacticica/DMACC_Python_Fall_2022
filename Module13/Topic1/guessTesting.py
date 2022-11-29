import unittest
from Module13.Topic1 import guessGame as g



class UnitTesting(unittest.TestCase):

    def setUp(self):
        self.newList = g.NumberGuesser()

    def tearDown(self):
        del self.newList

    def test_constructor(self):
        self.assertEqual(self.newList.guessed_list, [])
        self.assertEqual(self.newList.random_number, 0)

    def test_add_guess(self):
        with self.assertRaises(ValueError):
            #random number should still be 0
            self.newList.add_guess(0)
