class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, pnum, addy=''):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = pnum

    def display(self):
        return (f"{self.first_name} {self.last_name}\n{self.phone_number}\n{self.address}")
