import my_definitions as md

'''
Program: use_definitions_module.py
Author: Reagan Zierke
Last date modified: 10/25/22

This program tests a module by using the functions created for that module.
'''


name = 'Reagan'
md.greeting(name)

md.author()

new_set = {"Iron Man", "Spider-Man", "Captain America"}
md.print_set(new_set)

new_dict = {"Spider-Man" : "Peter Parker", "Iron Man" : "Tony Stark", "Captain America" : "Steve Rogers"}
md.print_dict(new_dict)
