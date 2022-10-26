from definitions import greetings, dict_op, set_op

'''
Program: use_pkgs.py
Author: Reagan Zierke
Last date modified: 10/26/22

This program tests importing modules from a package.
'''


name = 'Reagan'
greetings.greeting(name)

greetings.author()

new_set = {"Iron Man", "Spider-Man", "Captain America"}
set_op.print_set(new_set)

new_dict = {"Spider-Man" : "Peter Parker", "Iron Man" : "Tony Stark", "Captain America" : "Steve Rogers"}
dict_op.print_dict(new_dict)
