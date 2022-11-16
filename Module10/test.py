import unittest

from class_definitions import student as t

'''
Program: test.py
Author: Reagan Zierke
Last date modified: 11/02/22

This program tests multiple error cases that can possibly be created by the file student.py
'''
class UnitTesting(unittest.TestCase):

    def setUp(self):
        self.student = t.Student("Parker", 'Peter', 'AcDec')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, "Parker")
        self.assertEqual(self.student.first_name, "Peter")
        self.assertEqual(self.student.major, "AcDec")

    def test_object_created_all_attributes(self):
        student = t.Student('Parker', 'Peter', 'AcDec', '4.0')
        assert student.last_name == "Parker"
        assert student.first_name == "Peter"
        assert student.major == "AcDec"
        assert student.gpa == "4.0"

    def test_student_str(self):
        t.Student.__str__(self.student)



    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = t.Student("4.0", "Peter", "AcDec")


    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = t.Student("Parker", "4.2", "AcDec")

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = t.Student("Parker", "Peter", "4.1")

    def test_object_not_created_error_gpa1(self):
        with self.assertRaises(ValueError):
            s = t.Student("Parker", "Peter", "AcDec", 343)

    def test_object_not_created_error_gpa2(self):
        with self.assertRaises(ValueError):
            s = t.Student("Parker", "Peter", "AcDec", 5.3)
