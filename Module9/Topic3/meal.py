import tkinter

'''
Program: meals.py
Author: Reagan Zierke
Last date modified: 10/26/22

This program creates a gui where the user selects their favorite meal.
'''

#Define functions

def pick_breakfast():
    label.config(text="Breakfast do be good.") #changes the label in row 5

def pick_2breakfast():
    label.config(text="What even is a second breakfast?")

def pick_lunch():
    label.config(text="You eat lunch?!")

def pick_dinner():
    label.config(text="This is the best meal.")


#Creates window
m = tkinter.Tk()

#Title
m.title("Favorite Meal")

#Creates checkboxes
var1 = tkinter.IntVar() #notice we create an integer variable
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=1)

var2 = tkinter.IntVar() #notice we create an integer variable
check = tkinter.Checkbutton(m, text="2nd Breakfast", variable=var2, command=pick_2breakfast).grid(row=2)

var3 = tkinter.IntVar() #notice we create an integer variable
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch).grid(row=3)

var4 = tkinter.IntVar() #notice we create an integer variable
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_dinner).grid(row=4)

#Status
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)



#Exit Button
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)





m.mainloop()
