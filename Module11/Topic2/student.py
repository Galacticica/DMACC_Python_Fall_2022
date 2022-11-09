from Module11.Topic2.person import Person

'''
Program: student.py
Author: Reagan Zierke
Last date modified: 11/09/22

This program creates a student class that inherits the person class and takes input in the function that then allows the user to change the major, gpa, and display the students info
'''

class Student(Person):
    def __init__(self, sid, lname, fname, major='Computer Science', gpa=0.0, addy=''):
        #Initializes Person using the input given
        super().__init__(lname, fname, addy)
        self.major = major
        self.gpa = gpa
        self.student_id = sid

    def display(self):
        return Person.display(self) + "\nStudent ID: " + str(self.student_id) + "\nMajor: " + self.major + "\nCurrent GPA: " + str(self.gpa)

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa



if __name__ == "__main__":
    # Driver
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student
