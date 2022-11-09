from Module11.Topic1.person import Person
from datetime import datetime

'''
Program: student.py
Author: Reagan Zierke
Last date modified: 11/09/22

This program creates a student class that takes in a person object aswell as other input and then allows the user to change the major, gpa, and display the students info
'''

class Student:
    def __init__(self, human, major, gpa, sdate):
        #Creates a class called student with human object derived from person class aswell as major, gpa, and start date variables
        self.human = human
        self.major = major
        self.gpa = gpa
        if "/" in sdate:
            self.start_date = datetime.strptime(sdate, '%m/%d/%Y').strftime("%m/%d/%Y")
        else:
            self.start_date = datetime.strptime(sdate, '%m-%d-%Y').strftime("%m/%d/%Y")

    def display(self):
        return str(self.human.display()) + "\nStart Date: " + self.start_date + "\nMajor: " + self.major + "\nCurrent GPA: " + self.gpa

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa



if __name__ == "__main__":
    #Driver
    #Creates person object
    p = Person('Zierke', 'R', '1001 100th Street, IA')
    #Creates student object
    s = Student(p, "Computer Science", '4.0', "11/09/2022")
    print(s.display())
    print("\n") #new line for clarity
    s.update_gpa('3.0')
    s.change_major("Being Awesome")
    print(s.display())
    del s
