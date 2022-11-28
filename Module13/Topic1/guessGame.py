import tkinter
from tkinter import *
from random import randint

class NumberGuesser:
    def __init__(self):
        self.guessed_list = []

    def reset_guesses(self):
        self.guessed_list = []

    def add_guess(self, guess):
        self.guessed_list.append(guess)






def start_game():
    guess1['state'] = NORMAL
    guess2['state'] = NORMAL
    guess3['state'] = NORMAL
    guess4['state'] = NORMAL
    guess5['state'] = NORMAL
    guess6['state'] = NORMAL
    guess7['state'] = NORMAL
    guess8['state'] = NORMAL
    guess9['state'] = NORMAL
    random_number = randint(1, 9)
    guess_list.reset_guesses()

def guessNumber_1():
    guess_list.add_guess(1)
    if random_number == 1:
        #winner
        pass
    else:
        guess1['state'] = DISABLED

def guessNumber_2():
    guess_list.add_guess(2)
    if random_number == 2:
        #winner
        pass
    else:
        guess1['state'] = DISABLED

def guessNumber_3():
    guess_list.add_guess(3)
    if random_number == 3:
        #winner
        pass
    else:
        guess1['state'] = DISABLED

def guessNumber_4():
    guess_list.add_guess(4)
    if random_number == 4:
        #winner
        pass
    else:
        guess1['state'] = DISABLED

def guessNumber_5():
    guess_list.add_guess(5)
    if random_number == 5:
        #winner
        pass
    else:
        guess1['state'] = DISABLED

def guessNumber_6():
    guess_list.add_guess(6)
    if random_number == 6:
        #winner
        pass
    else:
        guess1['state'] = DISABLED

def guessNumber_7():
    guess_list.add_guess(7)
    if random_number == 7:
        #winner
        pass
    else:
        guess1['state'] = DISABLED

def guessNumber_8():
    guess_list.add_guess(8)
    if random_number == 8:
        #winner
        pass
    else:
        guess1['state'] = DISABLED

def guessNumber_9():
    guess_list.add_guess(9)
    if random_number == 9:
        #winner
        pass
    else:
        guess1['state'] = DISABLED





random_number = 0
guess_list = NumberGuesser()

game = tkinter.Tk()

game.title("Guessing Game")

start_button = tkinter.Button(game, text = "Start", width = 5, height = 2, command=start_game)
start_button.grid(row = 0,
                  column = 2)

guess1 = tkinter.Button(game, text = "1", width = 2, height = 2, state = DISABLED)
guess1.grid(row = 2, column = 0)
guess2 = tkinter.Button(game, text = "2", width = 2, height = 2, state = DISABLED)
guess2.grid(row = 2, column = 2)
guess3 = tkinter.Button(game, text = "3", width = 2, height = 2, state = DISABLED)
guess3.grid(row = 2, column = 4)
guess4 = tkinter.Button(game, text = "4", width = 2, height = 2, state = DISABLED)
guess4.grid(row = 4, column = 0)
guess5 = tkinter.Button(game, text = "5", width = 2, height = 2, state = DISABLED)
guess5.grid(row = 4, column = 2)
guess6 = tkinter.Button(game, text = "6", width = 2, height = 2, state = DISABLED)
guess6.grid(row = 4, column = 4)
guess7 = tkinter.Button(game, text = "7", width = 2, height = 2, state = DISABLED)
guess7.grid(row = 6, column = 0)
guess8 = tkinter.Button(game, text = "8", width = 2, height = 2, state = DISABLED)
guess8.grid(row = 6, column = 2)
guess9 = tkinter.Button(game, text = "9", width = 2, height = 2, state = DISABLED)
guess9.grid(row = 6, column = 4)

exit_button = tkinter.Button(game, text='Exit', width=5, height = 2, command=game.destroy)
exit_button.grid(row = 8, column = 2)



game.mainloop()
