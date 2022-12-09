from Final_Project import person_class as p

import unittest

class unitTesting(unittest.TestCase):

    def setUp(self) -> None:
        self.player = p.Person("Galacticica", 'normal')

    def tearDown(self) -> None:
        del self.player

    def testValidPlayer(self):
        self.assertEqual(self.player.username, 'Galacticica')
        self.assertEqual(self.player.difficulty, 'normal')

    def testInvalidDifficulty(self):
        with self.assertRaises(p.Not_Valid_Difficulty):
            s = p.Person("Bob", "extreme")

    def test_string(self):
        s = self.player.__str__()

    def test_repr(self):
        s = self.player.__repr__()
