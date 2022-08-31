'''
Program: average_scores.py
Author: Reagan Zierke
Last date modified: 08/31/22

This program asks users for multiple inputs to detertmine an average score profile.
'''

#defines sum function
def summ(num1, *args):
    total = num1
    for num in args:
        total = total + num
    return total

#Set constant for total scores
total_scores = 3

#Prompting user for outputs

    #asking user for first name
first_name = input("Enter your first name: ")

    #asking user for last name
last_name = input("Enter your last name: ")

    #asking user for age
age = int(float(input("Enter your age: ")))

    #asking user for scores (total_scores) times
score_one = int(input("Enter your first score: "))
score_two = int(input("Enter your second score: "))
score_three = int(input("Enter your third score: "))

#calculates sum of 3 scores
total = summ(score_one, score_two, score_three)

#calculates the average score
avg_score = total / total_scores

#prints the score profile
print(f"{last_name}, {first_name} age: {age: 3d} average grade: {avg_score: 5.2f}")


'''
Observations
When the scores 78, 67, and 87 are input, their average is output as 77.33, keeping only 2 decimal places in an otherwise infinite number
When the scores 1, 45, and 101 are input, their average is output as 49.00, adding 2 extra decimals after the decimal place so that it sticks with the formatting
'''
