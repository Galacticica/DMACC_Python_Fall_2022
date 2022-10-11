'''
Program: search_sort_list.py
Author: Reagan Zierke
Last date modified: 10/11/22

This program searches for an item in a list and sorts the list.
'''

list = [1, 4, 23, 53, 2, 5, 37, 293, 12]

def sort_list(list_to_sort):
    list_to_sort.sort()
    return list_to_sort

def search_list(list_to_search, number):
    index = list_to_search.index(number)
    return index


if __name__ == '__main__':
    print(sort_list(list))
    print(search_list(list, 5))
    print(search_list(list, 42))

