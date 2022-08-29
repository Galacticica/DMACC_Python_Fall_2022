"""
Program: casting.py
Author: Reagan Zierke
Last date modified: 08/29/22

The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""

#Asks user for shoe size, casts answer to an integer, and prints that value
shoe_size = input("Enter a shoe size: ")
shoe_size_1_year = int(shoe_size) + 1
print ("Shoe Size in 1 year: " + str(shoe_size_1_year))





#Asking for an input for # of pages in a book and storing as a variable
pages = int(input("Enter the number of pages in the book: "))
#Asking for an input for # of chapters storing it as a variable
#Also calculates the average pages per chapter and converts that to a string
pages_per_chapter = str(pages // int(input("Enter the number of chapters in the book: ")))
#Tells user the approximate pages per chapter
print(f"Each chapter contains approximately {pages_per_chapter} pages.")
