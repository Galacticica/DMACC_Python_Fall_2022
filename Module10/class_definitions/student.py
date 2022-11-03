'''
Program: student.py
Author: Reagan Zierke
Last date modified: 11/02/22

This program creates a student class taking first and last name, major, and gpa.
'''
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError

        try:
            if not isinstance(gpa, float):
                raise ValueError
            if not 0.0 <= gpa <= 5.0:
                raise ValueError
        except ValueError:
            pass
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)
