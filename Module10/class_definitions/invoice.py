'''
Program: employee.py
Author: Reagan Zierke
Last date modified: 11/02/22

This program creates an invoice class that takes a customers info and order.
It then allows for customers to add an item to their order and then ask for an invoice
'''

class Invoice:
    '''Invoice class'''
    #constructor code
    def __init__(self, iID, cID, lname, fname, pn, addy, iwp = "{}"):
        self.invoice_id = iID
        self.customer_id = cID
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pn
        self.address = addy
        if iwp == "{}":
            self.items_with_price = {}
        else:
            self.items_with_price = iwp

    #Adds new items to dictionary
    def add_item(self, item):
        self.items_with_price.update(item)

    #Creates an invoice by calculating tax and total price and then printing each item as well as the price, tax, and total
    def create_invoice(self):
        price = 0
        items = self.items_with_price.keys()
        for i in items:
            price = price + self.items_with_price.get(i)
        tax = 0.06 * price
        total_price = price + tax
        for key, item in self.items_with_price.items():
            print(f"{key}....${item:,.2f}")
        print(f"Tax....${tax:,.2f}\n"
              f"Total....${total_price:,.2f}")

    def __str__(self):
        return(f"Last Name: {self.last_name}\n"
               f"First Name: {self.first_name}\n"
               f"Phone Number: {self.phone_number}\n"
               f"Address: {self.address}\n"
               f"Customer ID: {self.customer_id}\n"
               f"Invoice ID: {self.invoice_id}")

    def __repr__(self):
        return(f"Last Name: {self.last_name}\n"
               f"First Name: {self.first_name}\n"
               f"Phone Number: {self.phone_number}\n"
               f"Address: {self.address}\n"
               f"Customer ID: {self.customer_id}\n"
               f"Invoice ID: {self.invoice_id}")



#driver code
if __name__ == "__main__":
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
