from datetime import datetime
'''

'''


class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, addy, pnum, hourly = "true", sdate = "1/1/2000", salary = "15"):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = pnum
        self.salaried = bool(hourly)
        self.salary = float(salary)
        if "/" in sdate:
            self.start_date = datetime.strptime(sdate, '%m/%d/%Y').strftime("%m/%d/%Y")
        else:
            self.start_date = datetime.strptime(sdate, '%m-%d-%Y').strftime("%m/%d/%Y")

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name)

# Driver
if __name__ == "__main__":
    emp = Employee('Ruiz', 'Matthew', "1234 100th St.\nJohnston, IA", "515-555-9824", "true" , "5-23-2022", "18")   # call the construtor, needs to have a first and last name in parameter
    print(emp.start_date)
