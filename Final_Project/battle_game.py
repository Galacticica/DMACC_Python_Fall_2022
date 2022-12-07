import random
import person_class
import profession_classes as pcs
import enemy_class
import tkinter
from tkinter import *















#creates game window and titles game
game = tkinter.Tk()
game.title("Battle Game")

#player enemy stat labels TODO: Change placeholders to actual variables and add commands, add borders
player_label = tkinter.Label(game, text=f"player variable", width=20, height=2, font=('Helvetica bold',20))
player_label.grid(row=0, column=0, columnspan=4)
enemy_label = tkinter.Label(game, text=f"enemy variable", width=20, height=2, font=('Helvetica bold',20))
enemy_label.grid(row=0, column=4, columnspan=4)
hp_label_1 = tkinter.Label(game, text="HP", width=5, height=5, font=('Helvetica bold',20))
hp_label_1.grid(row=1, column=0)
dmg_label_1 = tkinter.Label(game, text="DMG", width=5, height=5, font=('Helvetica bold',20))
dmg_label_1.grid(row=1, column=1)
str_label_1 = tkinter.Label(game, text="STR", width=5, height=5, font=('Helvetica bold',20))
str_label_1.grid(row=1, column=2)
stl_label_1 = tkinter.Label(game, text="STL", width=5, height=5, font=('Helvetica bold',20))
stl_label_1.grid(row=1, column=3)
hp_label_2 = tkinter.Label(game, text="HP", width=5, height=5, font=('Helvetica bold',20))
hp_label_2.grid(row=1, column=4)
dmg_label_2 = tkinter.Label(game, text="DMG", width=5, height=5, font=('Helvetica bold',20))
dmg_label_2.grid(row=1, column=5)
str_label_2 = tkinter.Label(game, text="STR", width=5, height=5, font=('Helvetica bold',20))
str_label_2.grid(row=1, column=6)
stl_label_2 = tkinter.Label(game, text="STL", width=5, height=5, font=('Helvetica bold',20))
stl_label_2.grid(row=1, column=7)



game.mainloop()
