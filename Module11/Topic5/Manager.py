from Module11.Topic5.Person import Person
from Module11.Topic5.Employee import Employee
from Module11.Topic4.salaried import Employee as PaidEmployee
from datetime import datetime

'''
Program: Manager.py
Author: Reagan Zierke
Last date modified: 11/09/22

This program creates a manager class that inherits properties from both an Employee class and a Person class. The class takes in information and then allows the user to create new employees under the manager and list all the employees off
'''

#Creates manager object
class Manager(Person, Employee):
    def __init__(self, lname, fname, pnum, salary, department='', start_date = "11/9/2022", addy = '', dreports = []):
        #Initializes inherited classes
        super(Person, self).__init__(salary, start_date)
        super().__init__(lname, fname, pnum, addy)
        #Initializes manager class
        self.department = department
        self.direct_reports = dreports


    def display(self):
        return f"{Person.display(self)}\n{Employee.display(self)}\nDepartment: {self.department}"


    def give_raise(self, new_salary):
        #Updates salary
        self.salary = new_salary

    def hire_employee(self, new_employee):
        self.direct_reports.append(new_employee)

    def list_employees(self):
        for worker in self.direct_reports:
            print(f"{worker.last_name}, {worker.first_name}\nPhone Number: {worker.phone_number}\nStart Date: {worker.start_date}\nSalary: ${worker.salary:,.2f} per year\n")

    def __str__(self):
        return f"{Person.display(self)}\n{Employee.display(self)}\nDepartment: {self.department}"

    def __repr__(self):
        return f"{Person.display(self)}\n{Employee.display(self)}\nDepartment: {self.department}"



if __name__ == "__main__":
    #Creates manager
    manager = Manager("Zierke", "Reagan", "515-555-5555", 40000, "Sales", "11/9/2022", "9908 Ashton Dr.\nJohnston, IA")
    print(manager.display())

    #Create 3 employees (i know they're manager objects I kept getting an error and after 45 minutes of trying to fix the error I decided it wasn't worth the stress in this scenario
    employee1 = Manager("Bonefas", "J", "515-444-4444", 35000, "Sales", "8/23/2022")
    employee2 = Manager("Schlueter", "H", "515-333-3333", 33250, "Sales", "10/12/2022")
    employee3 = Manager("Jambor", "G", "515-232-2323", 31500, "Sales", "9/24/2022")
    #Hire Employees (add to direct reports object of manager)
    manager.hire_employee(employee1)
    manager.hire_employee(employee2)
    manager.hire_employee(employee3)
    print('\n') #new line for clarity
    #List direct reports
    manager.list_employees()
    #Give manager a raise
    manager.give_raise(42000)
    print(manager.display())
