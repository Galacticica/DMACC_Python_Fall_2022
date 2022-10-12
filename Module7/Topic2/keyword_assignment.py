'''
Program: keyword_assignment.py
Author: Reagan Zierke
Last date modified: 10/11/22

This program uses keywords to filter out the first name, last name, and average score of the user
'''

def average_scores(*scores, **inputs):
    f_name = ""
    l_name = ""
    total = 0
    # Use *args for average calculation
    for key, value in inputs.items():
        if key == "first_name":
            f_name = value
        if key == "last_name":
            l_name = value
        if key == "major":
            course = value
    for num in scores:
        total += num
    gpa = total / len(scores)
    return (f"Result: name = {f_name} {l_name} gpa = {gpa: .2f} course = {course}")


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World domination'))
    print(average_scores(5, 3, 3, first_name='Gabe', last_name='Jamb', major='Band'))
    print(average_scores(2, 3, 3, 4, 4, first_name='Donny', last_name='Blaze', major='Python'))
