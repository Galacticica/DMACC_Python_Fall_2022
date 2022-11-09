class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):  # Constructor sets all to no value
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        if self.address == '':
            return str(self.last_name) + ", " + str(self.first_name)
        else:
            return str(self.last_name) + ", " + str(self.first_name) + " lives at " + str(self.address)
