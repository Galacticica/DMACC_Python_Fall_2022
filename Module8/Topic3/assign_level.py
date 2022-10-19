'''
Program: assign_level.py
Author: Reagan Zierke
Last date modified: 10/19/22

This program uses dictionaries to return the correct number of points awarded and returns an error value if no such case exists.
'''

def switch_level(level):
    levels = {"N":50, "B":150, "E":300, "A":500}
    return (str(levels.get(level, "No such level.")))


if __name__ == "__main__":
    print(switch_level("B"))
    print(switch_level("C"))
