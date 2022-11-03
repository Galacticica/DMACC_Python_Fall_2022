from datetime import datetime
'''
Program: employee.py
Author: Reagan Zierke
Last date modified: 11/02/22

This program creates an employee class that takes in employees info and salary and returns an employee profile when display method is called.
'''


class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, addy, pnum, salaried = "false", sdate = "1/1/2000", salary = "15"):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = pnum
        self.salaried = bool(salaried)
        self.salary = float(salary)
        if "/" in sdate:
            self.start_date = datetime.strptime(sdate, '%m/%d/%Y').strftime("%m/%d/%Y")
        else:
            self.start_date = datetime.strptime(sdate, '%m-%d-%Y').strftime("%m/%d/%Y")

    def display(self):
        if self.salaried == True:
            return (f"{self.first_name} {self.last_name}\n{self.address}\n{self.phone_number}\nSalaried Employee: ${self.salary:,.2f}/year\nStart Date: {self.start_date}")
        else:
            return (f"{self.first_name} {self.last_name}\n{self.address}\n{self.phone_number}\nHourly Employee: ${self.salary}/hour\nStart Date: {self.start_date}")

    def __str__(self):
        if self.salaried == True:
            return (f"{self.first_name} {self.last_name}\n{self.address}\n{self.phone_number}\nSalaried Employee: ${self.salary:,.2f}/year\nStart Date: {self.start_date}")
        else:
            return (f"{self.first_name} {self.last_name}\n{self.address}\n{self.phone_number}\nHourly Employee: ${self.salary}/hour\nStart Date: {self.start_date}")

    def __repr__(self):
        if self.salaried == True:
            return (f"{self.first_name} {self.last_name}\n{self.address}\n{self.phone_number}\nSalaried Employee: ${self.salary:,.2f}/year\nStart Date: {self.start_date}")
        else:
            return (f"{self.first_name} {self.last_name}\n{self.address}\n{self.phone_number}\nHourly Employee: ${self.salary}/hour\nStart Date: {self.start_date}")

# Driver
if __name__ == "__main__":
    emp = Employee('Ruiz', 'Matthew', "1234 100th St.\nJohnston, IA", "515-555-9824", "true" , "5-23-2022", "37000")   # call the construtor, needs to have a first and last name in parameter
    print(emp.display())
    print("\n")
    print(str(emp))
    print("\n")
    print(repr(emp))
    del emp
