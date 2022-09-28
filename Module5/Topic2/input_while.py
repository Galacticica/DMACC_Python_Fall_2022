'''
Program: input_while.py
Author: Reagan Zierke
Last date modified: 09/26/22

This program takes input 1-100 from the user and when the while loop is quit, prints each input that the user entered.
'''

#Declares user input list
userInputs = []
sent_val = 'continue'
#Asks user for inputs of 1-100 until they stop
while sent_val not in ['quit', 'q', 'exit', 'leave', 'stop']:
    sent_val = input("Enter a number 1-100: ").lower()
    try:
        userInt = int(sent_val)
        if userInt in range(1,100):
            userInputs.append(userInt)
        else:
            print("User's integer is outside of the allowed range")
    except:
        print("User did not input an integer")

#Prints each value that the user input
for x in userInputs:
    print(x)


'''
Inputs: 3, 23, 45, 102, 2, q
Results: NA, NA, NA, not in range, NA, stops loop
Outputs: 3, 23, 45, 2
'''
