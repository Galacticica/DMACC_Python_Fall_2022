'''
Program: input_while_exit.py
Author: Reagan Zierke
Last date modified: 09/28/22

This program takes input 1-100 from the user and when the while loop is quit, prints each input that the user entered.
'''

#Declares user input list
userInputs = []
stopInputs = ['quit', 'q', 'exit', 'leave', 'stop']
sent_val = 'continue'
stop = False
#Asks user for inputs of 1-100 until they stop
while sent_val not in stopInputs:
    while sent_val not in range(1,100):
        sent_val = input("Enter a number 1-100: ").lower()
        if sent_val in stopInputs:
            stop = True
            break
        sent_val = int(sent_val)
    if stop == True:
        break
    userInputs.append(sent_val)
    sent_val = 0

#Prints each value that the user input
for x in userInputs:
    print(x)


'''
Inputs: 3, 23, 45, 102, 2, q
Results: NA, NA, NA, not in range, NA, stops loop
Outputs: 3, 23, 45, 2
'''
