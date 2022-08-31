"""
Program: casting.py
Author: Reagan Zierke
Last date modified: 08/29/22

The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""

#Asks user for shoe size, casts answer to an integer, and prints that value
shoe_size = input("Enter a shoe size: ")
#Casts the input to a float and then an integer (as without the float cast if a float value is inputted it results in an error) and adds 1
shoe_size_1_year = int(float(shoe_size)) + 1
#prints shoe size in 1 year
print ("Shoe Size in 1 year: " + str(shoe_size_1_year))

"""
Input: 11
Expected Output: 12
Actual Output: 12

Input: 6.5
Expected Output: 7
Actual Output: 7

Input: potato
Expected Output: ?
Actual Output: ?
"""



#Asking for an input for # of pages in a book and storing as a variable
pages = int(input("Enter the number of pages in the book: "))
#Asking for an input for # of chapters storing it as a variable
#Also calculates the average pages per chapter and converts that to a string
pages_per_chapter = str(pages // int(input("Enter the number of chapters in the book: ")))
#Tells user the approximate pages per chapter
print(f"Each chapter contains approximately {pages_per_chapter} pages.")
