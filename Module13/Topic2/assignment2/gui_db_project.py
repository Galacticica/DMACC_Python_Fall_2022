from Module13.Topic2.assignment2 import createDB
from Module13.Topic2.assignment2 import writeDB
from Module13.Topic2.assignment2 import readDB
import tkinter
from tkinter import *



#defines constant for db name
db = "gui-db.db"
'''
Define functions/methods below here
'''
def create_student_person_tables():
    '''
    creates tables
    :return:
    '''
    createDB.create_tables(db)
    create_table_button['state'] = DISABLED

def insert_person():
    '''
    inserts person to table
    :return:
    '''
    conn = writeDB.create_connection(db)
    person = (first_name_input.get(), last_name_input.get())
    person_id = writeDB.create_person(conn, person)

def insert_student():
    '''
    inserts student to table
    :return:
    '''
    conn = readDB.create_connection(db)
    with conn:
        rows = readDB.select_all_students(conn)
        for row in rows:
            if (first_name_input.get()) in row and (last_name_input.get()) in row:
                person_id = row[0]
    student = (person_id, major_input.get(), start_date_input.get())
    student_id = writeDB.create_student(conn, student)

def read_persons():
    '''
    reads person data
    :return:
    '''
    conn = readDB.create_connection(db)
    with conn:
        rows = readDB.select_all_persons(conn)
        for row in rows:
            print(row)

def read_students():
    '''
    reads student data
    :return:
    '''
    conn = readDB.create_connection(db)
    with conn:
        rows = readDB.select_all_students(conn)
        for row in rows:
            print(row)

'''
Define functions/methods above here
'''

#create main window
m = tkinter.Tk()
x=0
'''
Insert module code below here
'''
##The Main Window Title that appears in the bar
m.title('Students Database') #replace this with whatever you would like

create_table_button = tkinter.Button(m, text="Create Tables", width = 25, command = create_student_person_tables)
create_table_button.grid(row=0)

first_name_label = tkinter.Label(m, text = "First Name:", width = 25)
first_name_label.grid(row=1, column=0)
first_name_input = tkinter.Entry(m, width=25)
first_name_input.grid(row=1, column=1)

last_name_label = tkinter.Label(m, text = "Last Name:", width = 25)
last_name_label.grid(row=2, column=0)
last_name_input = tkinter.Entry(m, width=25)
last_name_input.grid(row=2, column=1)

major_label = tkinter.Label(m, text = "Major:", width = 25)
major_label.grid(row=3, column=0)
major_input = tkinter.Entry(m, width=25)
major_input.grid(row=3, column=1)

start_date_label = tkinter.Label(m, text = "Start Date:", width=25)
start_date_label.grid(row=4,column=0)
start_date_input = tkinter.Entry(m, width=25)
start_date_input.grid(row=4,column=1)

create_person_button = tkinter.Button(m, text = "Create Person", width=25, command=insert_person)
create_person_button.grid(row=5, column=0)
create_student_button = tkinter.Button(m, text = "Create Student", width=25, command=insert_student)
create_student_button.grid(row=5, column=1)

show_person_button = tkinter.Button(m, text = "Show People", width=25, command=read_persons)
show_person_button.grid(row=6, column=0)
show_students_button = tkinter.Button(m, text = "Show Students", width=25, command=read_students)
show_students_button.grid(row=6, column=1)

##The Main window Exit/destroy function; Note Feel free to change it's "text='Exit'" to another
##     word like "text='Quit'" or whatever is relevent for you; as well as modify the width
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=x+7)

'''
Insert module code above here
'''
m.mainloop()


