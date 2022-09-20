'''
Program: employeeWage2.py
Author: Reagan Zierke
Last date modified: 09/19/22

This program prompts users for name, hours worked, and hourly wage, and prints out all the information.
'''

def weekly_wage(hours, wage):
    '''
    Calculates the weekly wage
    :param hours:
    :param wage:
    :return:
    '''
    week_wage = hours * wage
    return week_wage

def employee_info():
    '''
    Prompts user for name, hours worked, and wage
    '''
    #Asks for name
    name = input("What is your name? ")
    #Asks for hours worked
    hours_worked = input("How many hours did you work?")
    try:
        hours_worked = int(hours_worked)
        if (hours_worked >= 0):
            pass
        else:
            raise ValueError("Not a valid number of hours")
    except ValueError:
        print("Input is not a valid number")
    #Asks for hourly wage
    hourly_wage = input("What is your hourly wage?")
    try:
        hourly_wage = float(hourly_wage)
        if (hourly_wage > 0.00):
            pass
        else:
            raise ValueError("Not a valid wage")
    except ValueError:
        print("Input is not a valid number")
    week_wage = weekly_wage(hours_worked, hourly_wage)
    return(f"{name} worked {hours_worked} hours and earned ${week_wage: .2f}.")

if __name__ == "__main__":
    try:
        employee_wage = employee_info()
    except ValueError as err:
        print("Value error encountered")
    else:
        print(employee_wage)

