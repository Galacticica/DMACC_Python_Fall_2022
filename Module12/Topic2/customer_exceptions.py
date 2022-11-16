class Customer:
    '''Invoice class'''
    #constructor code
    def __init__(self, cID, lname, fname, pn):
        self.customer_id = cID
        try:
            if not isinstance(self.customer_id, int):
                raise InvalidCustomerIdException
            elif self.customer_id not in range(1000,9999):
                raise InvalidCustomerIdException
        except InvalidCustomerIdException:
            pass

        self.last_name = lname
        self.first_name = fname
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        try:
            if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
                raise InvalidNameException
        except InvalidNameException:
            pass

        self.phone_number = pn
        phone_characters = set("1234567890-")
        try:
            for x in self.phone_number:
                if x == 3 or x == 7:
                    if self.phone_number[x] != '-':
                        raise InvalidPhoneNumberFormat
                else:
                    try:
                        int(self.phone_number[x])
                    except:
                        raise InvalidPhoneNumberFormat
        except InvalidPhoneNumberFormat:
            pass

    def __str__(self):
        return(f"Last Name: {self.last_name}\n"
               f"First Name: {self.first_name}\n"
               f"Phone Number: {self.phone_number}\n"
               f"Customer ID: {self.customer_id}")

class InvalidCustomerIdException(Exception):
    '''Not a valid Customer ID'''
    pass

class InvalidNameException(Exception):
    '''Not a valid name'''
    pass

class InvalidPhoneNumberFormat(Exception):
    '''Not valid phone number formatting'''
    pass



if __name__ == "__main__":
    badID = Customer(1, "Zierke", "R", "515-444-4444")
    badLastName = Customer(1234, "P1WQ", "R", "515-444-4444")
    badFirstName = Customer(1234, "Zierke", "123", "515-444-4444")
    badPhone = Customer(1234, "Zierke", "R", "5155-51-4444")
    str(badID)
