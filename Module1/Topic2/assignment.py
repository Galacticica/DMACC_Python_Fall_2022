"""
Program: assignment.py
Author: Reagan Zierke
Last date modified: 08/26/22

The purpose of this program is to demonstrate knowledge of variables.
"""
import constants

#Set variable for item
item = "drumsticks"
#Set variable for quantity of item
quantity = 3
#Set variable for size of item
size = 5.0
#Concatonate string together
final_string = (str(quantity) + ' ' + item + ' size ' + str(size))
#Print String
print(final_string)

#Add price of item via constant
final_string = (str(quantity) + ' ' + item + ' size ' + str(size) +'\n' + item + ' cost ' + str(constants.price))
print(final_string)

#Same thing with f string
final_string = f"{str(quantity)} {item} size {str(size)}\n{item} cost {str(constants.price)}"
print(final_string)
