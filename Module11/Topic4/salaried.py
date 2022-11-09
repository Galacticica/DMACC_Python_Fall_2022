from datetime import datetime
from Module11.Topic4.employee import Employee

'''
Program: salaried.py
Author: Reagan Zierke
Last date modified: 11/09/22

This program creates a class for salaried employees, inheriting the employee class. It then allows the user to display the employee or update the employee's salary.
'''

class SalariedEmployee(Employee):
    def __init__(self, lname, fname, addy, pnum, salary=50000, sdate=11/9/2022):
        super().__init__(lname, fname, pnum, addy)
        self.salary = salary
        #Formats date correctly
        if "/" in sdate:
            self.start_date = datetime.strptime(sdate, '%m/%d/%Y').strftime("%m/%d/%Y")
        else:
            self.start_date = datetime.strptime(sdate, '%m-%d-%Y').strftime("%m/%d/%Y")

    def display(self):
        #return string
        return f"{Employee.display(self)}\nStart Date: {self.start_date}\nSalary: ${self.salary:,.2f} per year"

    def give_raise(self, new_salary):
        #Updates salary
        self.salary = new_salary


#Driver code
if __name__ == "__main__":
    #creates object new_employee
    new_employee = SalariedEmployee('Zierke', 'Reagan', '515-555-5555', '10010 100th Street\nJohnston, IA', 40000, '11/9/2022')
    print(new_employee.display())
    print('\n') #new line for clarity
    #updates salary
    new_employee.give_raise(45000)
    print(new_employee.display())
