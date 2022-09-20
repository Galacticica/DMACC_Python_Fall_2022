'''
Program: employeeWage2.py
Author: Reagan Zierke
Last date modified: 09/20/22

This program takes a string and a number and then prints the string that number of times.
'''


def multiply_string(string, number):
    '''
    Returns string x number of times
    :param string:
    :param number:
    :return:
    '''
    multiple_string = string*number
    return multiple_string


if __name__ == '__main__':
    string = input("Enter a phrase: ")
    try:
        integer = int(input("How many times would you like your string printed? "))
        if integer > 0:
            pass
        else:
            raise ValueError
    except ValueError as err:
        print("ValueError found")
    else:
        print(multiply_string(string, integer))
