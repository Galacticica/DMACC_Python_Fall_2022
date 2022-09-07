'''
Program: packageList.py
Author: Reagan Zierke
Last date modified: 09/07/22

This program gives the user information about the different packages for the Programmer's Toolkit Monthly Subscription Box
'''

#Prints information about toolkit
print("Thank you for your interest in the Programmer's Toolkit Monthly Subscription Box."
      "\nEach month we offer a selection of t-shirts, stickers, figurines, even programming books."
      "\nThe following are the packages that we offer."
      "\n1. Free Trial"
      "\n2. Bronze"
      "\n3. Silver"
      "\n4. Gold"
      "\n5. Platinum")

#Asks user which one they'd like to hear about
package = int(input("Please enter the number that corresponds with the package you'd like to here the price for."))


#The following is a conditional statement to give the user the price for the correct package that they chose
if package == 1:
    print("The free trial is free of course.")
elif package == 2:
    print("The bronze package costs $30")
elif package == 3:
    print("The silver package costs $40.")
elif package == 4:
    print("The gold package costs $50")
elif package == 5:
    print("The platinum package costs $60.")
else:
    print("That is not a valid package.")


'''
Tests

Input: 2
Expected Output: The bronze package costs $30
Actual Output: The bronze package costs $30

Input: 1
Expected Output: The free trial is free of course.
Actual Output: The free trial is free of course.

Input: 6
Expected Output: That is not a valid package.
Actual Output: That is not a valid package.

Input: Bronze
Expected Output: Error
Actual Output: Error
'''
