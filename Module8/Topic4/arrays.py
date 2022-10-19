'''
Program: arrays.py
Author: Reagan Zierke
Last date modified: 10/19/22

This program works with arrays to search and sort one.
'''

import array as arr

number_array = arr.array("i",[1, 3, 7, 13, 41, 31, 37, 12, 73])

def search_array(value):
    try:
        index = number_array.index(value)
    except:
        index = -1
    print (index)


def sort_array():
    number_list = number_array.tolist()
    number_list.sort()
    sorted_array = arr.array('i', number_list)
    return sorted_array
    #Included return statement because otherwise the new sorted array will stay within this function and be lost if the function is called again






if __name__ == "__main__":
    print (number_array)
    search_array(12)
    search_array(4)
    sorted_array = sort_array()
    print (sorted_array)
