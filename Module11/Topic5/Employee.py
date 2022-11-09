from datetime import datetime
from Module11.Topic5.Person import Person


class Employee():
    def __init__(self, salary=50000, sdate=11/9/2022):
        self.salary = salary
        #Formats date correctly
        if "/" in sdate:
            self.start_date = datetime.strptime(sdate, '%m/%d/%Y').strftime("%m/%d/%Y")
        else:
            self.start_date = datetime.strptime(sdate, '%m-%d-%Y').strftime("%m/%d/%Y")

    def display(self):
        #return string
        return f"Start Date: {self.start_date}\nSalary: ${self.salary:,.2f} per year"

    def give_raise(self, new_salary):
        #Updates salary
        self.salary = new_salary



    def __str__(self):
        return (f"Employee: ${self.salary:,.2f}/year\nStart Date: {self.start_date}")

    def __repr__(self):
        return (f"Employee: ${self.salary:,.2f}/year\nStart Date: {self.start_date}")
