from Final_Project import enemy_class as e
import unittest


class UnitTests(unittest.TestCase):

    def setUp(self) -> None:
        self.c = e.Enemy()

    def tearDown(self) -> None:
        del self.c

    def testValidEnemy(self):
        self.assertEqual(self.c.health, 0)
        self.assertEqual(self.c.damage, 0)
        self.assertEqual(self.c.strength, 0)
        self.assertEqual(self.c.stealth, 0)

    def testRandomEnemy(self):
        self.c.new_enemy()
        self.assertNotEqual(self.c.health, 0)
        self.assertNotEqual(self.c.damage, 0)
        self.assertNotEqual(self.c.strength, 0)
        self.assertNotEqual(self.c.stealth, 0)

    def test_string(self):
        s = self.c.__str__()

    def test_repr(self):
        s = self.c.__repr__()
