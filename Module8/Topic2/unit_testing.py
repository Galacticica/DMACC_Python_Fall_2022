import unittest

import self as self

from Module8.Topic2.test_scores import average_scores

class MyTestCase(unittest.TestCase):

    def test_average(self):
        # Arrange
        self.scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.6666666  # 7 decimal places, remove one and see the test fail
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual, places = 2)


    def test_average_5(self):
        # Arrange
        self.scores_dict = {"Test 1": 69, "Test 2": 84, "Test 3": 74, "Test 4": 99, "Test 5": 100}
        expected = 85.2  # 7 decimal places, remove one and see the test fail
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual, places = 4)

    def test_average_zero(self):
        # Arrange
        self.scores_dict = {}
        expected = 39.6666666  # 7 decimal places, remove one and see the test fail
        # Act
        # Assert
        with self.assertRaises(ValueError):
            average_scores(self.scores_dict)
