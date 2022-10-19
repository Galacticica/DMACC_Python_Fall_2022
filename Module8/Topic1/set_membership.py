'''
Program: set_membership.py
Author: Reagan Zierke
Last date modified: 10/19/22

This program takes input of a set and an object and checks if that object is in the set.
'''


def test_set(set, object):
    if object in set:
        print(f"{object} is in the set {str(set)}.")
    else:
        print(f"{object} is not in the set {str(set)}.")




if __name__ == "__main__":
    a_set = {'cat', 'dog', 'monkey'}
    test_set(a_set, 'cat')
    test_set(a_set, 'fish')
