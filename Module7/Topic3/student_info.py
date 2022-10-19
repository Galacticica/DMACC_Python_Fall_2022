'''
Program: student_info.py
Author: Reagan Zierke
Last date modified: 10/12/22

This program prompts the user for student scores and then writes it to a seperate text file
'''



def get_student_info(student_name):
    '''
    Takes scores from the user until the sent_val is input
    Sends students name and scores off to be written to a file
    :param student_name: the students name
    '''
    student_scores = []
    sent_val = 'continue'
    while sent_val not in ['quit', 'q', 'exit', 'leave', 'stop']:
        sent_val = input(f"Enter score for {student_name}: ").lower()
        try:
            newScore = int(sent_val)
            student_scores.append(newScore)
        except:
            if sent_val in ['quit', 'q', 'exit', 'leave', 'stop']:
                pass
            else:
                print("User did not input an integer")
    student_data = (student_name, student_scores)
    write_to_file(student_data)

def write_to_file(student_data):
    '''
    writes student data to a seperate file
    :param student_data: data from the get_student_info function
    '''
    file = open('student_info.txt', 'a')
    file.write(student_data[0] + ': ' + str(student_data[1]) + '\n')
    file.close()




def read_file():
    '''
    reads the students data from the external file
    '''
    with open("student_info.txt") as file:
        for line in file:
            print(line.rstrip())
    file.close()











if __name__ == '__main__':
    open("student_info.txt","w").close()
    #Ask for 4 students info
    get_student_info('Ben')
    get_student_info('Johanna')
    get_student_info('Gabe')
    get_student_info('Peyton')
    #prints out students info
    read_file()
