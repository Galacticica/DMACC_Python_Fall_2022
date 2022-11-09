from Module11.Topic5.Person import Person
from Module11.Topic5.Employee import Employee
from Module11.Topic4.salaried import Employee as PaidEmployee
from datetime import datetime


#Creates manager object
class Manager(Person, Employee):
    def __init__(self, lname, fname, pnum, salary, department, start_date = "11/9/2022", addy = '', dreports = []):
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



if __name__ == "__main__":
    #Creates manager
    manager = Manager("Zierke", "Reagan", "515-555-5555", 40000, "Sales", "11/9/2022", "9908 Ashton Dr.\nJohnston, IA")
    print(manager.display())


    #Creates 3 new employees for manager
