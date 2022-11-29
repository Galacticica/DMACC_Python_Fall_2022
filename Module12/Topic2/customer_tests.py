import unittest
from Module12.Topic2 import customer_exceptions as c

class UnitTesting(unittest.TestCase):

    def setUp(self):
        self.customer = c.Customer(1000, "Zierke", "R", "515-444-4444")

    def tearDown(self):
        del self.customer

    def test_valid_customer(self):
        self.assertEqual(self.customer.customer_id, 1000)
        self.assertEqual(self.customer.last_name, "Zierke")
        self.assertEqual(self.customer.first_name, "R")
        self.assertEqual(self.customer.phone_number, "515-444-4444")

    def test_invalid_customer_id(self):
        with self.assertRaises(c.InvalidCustomerIdException):
            s = c.Customer(10023344, "Zierke", "R", "515-444-4444")

    def test_invalid_last_name(self):
        with self.assertRaises(c.InvalidNameException):
            s = c.Customer(1000, "Pq2w", "R", "515-444-4444")

    def test_invalid_first_name(self):
        with self.assertRaises(c.InvalidNameException):
            s = c.Customer(1000, "Zierke", "32", "515-444-4444")

    def test_invalid_phone_number(self):
        with self.assertRaises(c.InvalidPhoneNumberFormat):
            s = c.Customer(1000, "Zierke", "R", "55-34344-32")

    def test_customer_str(self):
        s = c.Customer.__str__(self.customer)
