import tkinter
from tkinter import *
from random import randint


class NumberGuesser:
    def __init__(self):
        self.guessed_list = []
        self.random_number = 0

    def reset_guesses(self):
        self.guessed_list = []

    def add_guess(self, guess):
        try:
            if guess == self.random_number:
                raise ValueError
        except ValueError:
            pass
        self.guessed_list.append(guess)

    def get_random_number(self):
        self.random_number = randint(1,9)


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
    guess_list.reset_guesses()
    guess_list.get_random_number()
    output.config(text="")

def disable_all():
    guess1['state'] = DISABLED
    guess2['state'] = DISABLED
    guess3['state'] = DISABLED
    guess4['state'] = DISABLED
    guess5['state'] = DISABLED
    guess6['state'] = DISABLED
    guess7['state'] = DISABLED
    guess8['state'] = DISABLED
    guess9['state'] = DISABLED

def guessNumber_1():
    guess_list.add_guess(1)
    if guess_list.random_number == 1:
        output.config(text="WINNER!")
        disable_all()
    else:
        if guess_list.random_number > 1:
            output.config(text="Higher")
        elif guess_list.random_number < 1:
            output.config(text="Lower")
        guess1['state'] = DISABLED


def guessNumber_2():
    guess_list.add_guess(2)
    if guess_list.random_number == 2:
        output.config(text="WINNER!")
        disable_all()
    else:
        if guess_list.random_number > 2:
            output.config(text="Higher")
        elif guess_list.random_number < 2:
            output.config(text="Lower")
        guess2['state'] = DISABLED


def guessNumber_3():
    guess_list.add_guess(3)
    if guess_list.random_number == 3:
        output.config(text="WINNER!")
        disable_all()
    else:
        if guess_list.random_number > 3:
            output.config(text="Higher")
        elif guess_list.random_number < 3:
            output.config(text="Lower")
        guess3['state'] = DISABLED


def guessNumber_4():
    guess_list.add_guess(4)
    if guess_list.random_number == 4:
        output.config(text="WINNER!")
        disable_all()
    else:
        if guess_list.random_number > 4:
            output.config(text="Higher")
        elif guess_list.random_number < 4:
            output.config(text="Lower")
        guess4['state'] = DISABLED


def guessNumber_5():
    guess_list.add_guess(5)
    if guess_list.random_number == 5:
        output.config(text="WINNER!")
        disable_all()
    else:
        if guess_list.random_number > 5:
            output.config(text="Higher")
        elif guess_list.random_number < 5:
            output.config(text="Lower")
        guess5['state'] = DISABLED


def guessNumber_6():
    guess_list.add_guess(6)
    if guess_list.random_number == 6:
        output.config(text="WINNER!")
        disable_all()
    else:
        if guess_list.random_number > 6:
            output.config(text="Higher")
        elif guess_list.random_number < 6:
            output.config(text="Lower")
        guess6['state'] = DISABLED


def guessNumber_7():
    guess_list.add_guess(7)
    if guess_list.random_number == 7:
        output.config(text="WINNER!")
        disable_all()
    else:
        if guess_list.random_number > 7:
            output.config(text="Higher")
        elif guess_list.random_number < 7:
            output.config(text="Lower")
        guess7['state'] = DISABLED


def guessNumber_8():
    guess_list.add_guess(8)
    if guess_list.random_number == 8:
        output.config(text="WINNER!")
        disable_all()
    else:
        if guess_list.random_number > 8:
            output.config(text="Higher")
        elif guess_list.random_number < 8:
            output.config(text="Lower")
        guess8['state'] = DISABLED


def guessNumber_9():
    guess_list.add_guess(9)
    if guess_list.random_number == 9:
        output.config(text="WINNER!")
        disable_all()
    else:
        if guess_list.random_number > 9:
            output.config(text="Higher")
        elif guess_list.random_number < 9:
            output.config(text="Lower")
        guess9['state'] = DISABLED


random_number = 0
guess_list = NumberGuesser()

game = tkinter.Tk()

game.title("Guessing Game")

start_button = tkinter.Button(game, text="Start", width=10, height=5, command=start_game, font=('Helvetica bold',20))
start_button.grid(row=0,
                  column=2)

guess1 = tkinter.Button(game, text="1", width=5, height=5, state=DISABLED, command=guessNumber_1)
guess1.grid(row=2, column=0)
guess2 = tkinter.Button(game, text="2", width=5, height=5, state=DISABLED, command=guessNumber_2)
guess2.grid(row=2, column=2)
guess3 = tkinter.Button(game, text="3", width=5, height=5, state=DISABLED, command=guessNumber_3)
guess3.grid(row=2, column=4)
guess4 = tkinter.Button(game, text="4", width=5, height=5, state=DISABLED, command=guessNumber_4)
guess4.grid(row=4, column=0)
guess5 = tkinter.Button(game, text="5", width=5, height=5, state=DISABLED, command=guessNumber_5)
guess5.grid(row=4, column=2)
guess6 = tkinter.Button(game, text="6", width=5, height=5, state=DISABLED, command=guessNumber_6)
guess6.grid(row=4, column=4)
guess7 = tkinter.Button(game, text="7", width=5, height=5, state=DISABLED, command=guessNumber_7)
guess7.grid(row=6, column=0)
guess8 = tkinter.Button(game, text="8", width=5, height=5, state=DISABLED, command=guessNumber_8)
guess8.grid(row=6, column=2)
guess9 = tkinter.Button(game, text="9", width=5, height=5, state=DISABLED, command=guessNumber_9)
guess9.grid(row=6, column=4)

output = tkinter.Label(game, text="", width=10, height=5, font=('Helvetica bold',20))
output.grid(row=8, column=2)

exit_button = tkinter.Button(game, text='Exit', width=10, height=5, command=game.destroy, font=('Helvetica bold',20))
exit_button.grid(row=10, column=2)

game.mainloop()
