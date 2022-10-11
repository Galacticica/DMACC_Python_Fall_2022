'''
Program: basic_list.py
Author: Reagan Zierke
Last date modified: 10/11/22

This program takes input from the user (num) times and then prints out integers in a list.
'''

def make_list(num):
    '''
    Makes a list by running a loop num times for input and then takes integers and adds them to the list
    :param num: number of times the loop should run
    '''
    #empty list
    list = []
    x = 0
    #asks user for input num times
    while x in range (0, num):
        newNumber = get_input()
        try:
            newNumber = int(newNumber)
            list.append(newNumber)
        except:
            pass
        x=x+1
    return list

def get_input():
    '''
    Asks user for a number
    :return: input given
    '''
    newNumber = input("Enter a number: ")
    return newNumber








if __name__ == '__main__':
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))

