from random import randint
import person_class
import profession_classes as pcs
import enemy_class
import tkinter
from tkinter import *


'''Functions'''

def easy_chosen():
    '''selects difficulty indicated by button pressed'''
    global difficulty
    difficulty = 'easy'
    easy_select['state'] = DISABLED
    normal_select['state'] = DISABLED
    hard_select['state'] = DISABLED
    warrior_select.grid(row=4, column=1)
    ranger_select.grid(row=4, column=3)

def normal_chosen():
    '''selects difficulty indicated by button pressed'''
    global difficulty
    difficulty = 'normal'
    easy_select['state'] = DISABLED
    normal_select['state'] = DISABLED
    hard_select['state'] = DISABLED
    warrior_select.grid(row=4, column=1)
    ranger_select.grid(row=4, column=3)

def hard_chosen():
    '''selects difficulty indicated by button pressed'''
    global difficulty
    difficulty = 'hard'
    easy_select['state'] = DISABLED
    normal_select['state'] = DISABLED
    hard_select['state'] = DISABLED
    warrior_select.grid(row=4, column=1)
    ranger_select.grid(row=4, column=3)


def warrior_chosen():
    '''selects class indicated by button pressed'''
    global chosen_class
    chosen_class = "warrior"
    warrior_select['state'] = DISABLED
    ranger_select['state'] = DISABLED
    begin_button.grid(row=6, column=2)

def ranger_chosen():
    '''selects class indicated by button pressed'''
    global chosen_class
    chosen_class = "ranger"
    warrior_select['state'] = DISABLED
    ranger_select['state'] = DISABLED
    begin_button.grid(row=6, column=2)

def set_up_game():
    '''This function sets up the player and enemy objects, and updates the GUI'''
    global player_1
    global enemy_1
    username = str(username_input.get())
    if chosen_class == 'warrior':
        player_1 = pcs.Warrior(username, difficulty)
    elif chosen_class == 'ranger':
        player_1 = pcs.Ranger(username, difficulty)
    else:
        raise ValueError
    start_screen.destroy()
    enemy_1.new_enemy()
    player_label.config(text=f'{player_1.username}')
    player_hp.config(text=f'{player_1.health: .1f}')
    player_dmg.config(text=f'{player_1.damage}')
    player_str.config(text=f'{player_1.strength}')
    player_stl.config(text=f'{player_1.stealth}')
    enemy_label.config(text=f'{enemy_1.name}')
    enemy_hp.config(text=f'{enemy_1.health: .1f}')
    enemy_dmg.config(text=f'{enemy_1.damage}')
    enemy_str.config(text=f'{enemy_1.strength}')
    enemy_stl.config(text=f'{enemy_1.stealth}')

def potion_used():
    '''This function adds 30 health to the players hp if they use the item. It then checks if they have any left'''
    global player_1
    global health_potions_left
    player_1.health = player_1.health + 30
    player_hp.config(text=f'{player_1.health: .1f}')
    health_potions_left = health_potions_left-1
    if health_potions_left <= 0:
        heal_button['state'] = DISABLED
    action_display.config(text="You healed 30 health")

def steroid_used():
    global player_1
    global steroids_left
    player_1.strength = player_1.strength + 1
    player_str.config(text=f'{player_1.strength}')
    steroids_left = False
    enemy_attack(0)

def invis_used():
    global player_1
    global invis_left
    player_1.stealth = player_1.stealth + 1
    player_stl.config(text=f'{player_1.stealth}')
    invis_left = False
    enemy_attack(0)



def get_multiplier(current, opposing):
    '''
    This function is used to determine the attack multiplier based on strength and stealth
    :param current: current player attacking
    :param opposing: player being attacked
    :return: multiplier for calculation
    '''
    if current.strength > opposing.strength and current.stealth > opposing.stealth:
        multiplier = 1.5
    elif current.strength < opposing.strength and current.stealth < opposing.stealth:
        multiplier = 0.5
    elif current.strength > opposing.strength and current.stealth < opposing.stealth:
        multiplier = 1
    elif current.strength < opposing.strength and current.stealth > opposing.stealth:
        multiplier = 1
    elif current.strength > opposing.strength or current.stealth > opposing.stealth:
        multiplier = 1.25
    elif current.strength < opposing.strength or current.stealth < opposing.stealth:
        multiplier = 0.75
    else:
        multiplier = 1
    return multiplier


def new_enemy():
    '''This function gives the player a new enemy if they defeat the old one, assuming they want a new enemy'''
    global enemy_1
    global player_1

    def health_bonus():
        more_health_bonus_total = player_1.strength + player_1.stealth
        while more_health_bonus_total > 0:
            health_chance = randint(1,3)
            if health_chance == 1:
                player_1.health = player_1.health + 10
            more_health_bonus_total = more_health_bonus_total - 1
        player_hp.config(text=f'{player_1.health: .1f}')

    enemy_1.new_enemy()
    enemy_label.config(text=f'{enemy_1.name}')
    enemy_hp.config(text=f'{enemy_1.health: .1f}')
    enemy_dmg.config(text=f'{enemy_1.damage}')
    enemy_str.config(text=f'{enemy_1.strength}')
    enemy_stl.config(text=f'{enemy_1.stealth}')
    attack_button['state'] = NORMAL
    if health_potions_left > 0:
        heal_button['state'] = NORMAL
    if steroids_left is True:
        item1_button['state'] = NORMAL
    if invis_left is True:
        item2_button['state'] = NORMAL
    health_bonus()
    enemy_defeat.grid_remove()
    new_enemy_button.grid_remove()
    exit_win.grid_remove()



def player_attack():
    '''This function attacks the enemy with the players stats when the attack button is clicked'''
    global player_1
    global enemy_1
    multiplier_chance = randint(1, 3)
    if multiplier_chance == 2:
        multiplier = get_multiplier(player_1, enemy_1)
    else:
        multiplier = 1
    damage_dealt = player_1.damage * multiplier
    enemy_1.health = enemy_1.health - damage_dealt
    enemy_hp.config(text=f'{enemy_1.health : .1f}')
    if enemy_1.health <= 0:
        enemy_defeat.config(text=f'You defeated {enemy_1.name}')
        enemy_defeat.grid(row=5, columnspan=2, column=3)
        new_enemy_button.grid(row=6, column=3)
        exit_win.grid(row=6, column=4)
        attack_button['state'] = DISABLED
        item1_button['state'] = DISABLED
        item2_button['state'] = DISABLED
        heal_button['state'] = DISABLED
    else:
        enemy_attack(damage_dealt)

def enemy_attack(pd_dealt):
    '''This function attacks the player with the enemies stats'''
    global player_1
    global enemy_1
    attack_button['state'] = DISABLED
    item1_button['state'] = DISABLED
    item2_button['state'] = DISABLED
    multiplier_chance = randint(1, 3)
    if multiplier_chance == 2:
        multiplier = get_multiplier(enemy_1, player_1)
    else:
        multiplier = 1
    damage_dealt = enemy_1.damage * multiplier
    action_display.config(text=f"You dealt {pd_dealt} | {enemy_1.name} dealt {damage_dealt}")
    player_1.health = player_1.health - damage_dealt
    player_hp.config(text=f'{player_1.health: .1f}')
    if player_1.health <= 0:
        loser_label.grid(row=5, column=3, columnspan=2)
        exit_loser.grid(row=6, column=3, columnspan=2)

    else:
        attack_button['state'] = NORMAL
        if steroids_left is True:
            item1_button['state'] = NORMAL
        if invis_left is True:
            item2_button['state'] = NORMAL

'''Class Setup / Variable Setup'''
difficulty = ""
chosen_class = ""
player_1 = ''
enemy_1 = enemy_class.Enemy()
health_potions_left = 2
steroids_left = True
invis_left = True

'''GUI Windows'''


#creates game window and titles game

game = tkinter.Tk()
game.title("Battle Game")

#player enemy stat labels -
player_label = tkinter.Label(game, text=f"-", width=20, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
player_label.grid(row=0, column=0, columnspan=4)
enemy_label = tkinter.Label(game, text=f"-", width=20, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
enemy_label.grid(row=0, column=4, columnspan=4)
hp_label_1 = tkinter.Label(game, text="HP", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
hp_label_1.grid(row=1, column=0)
dmg_label_1 = tkinter.Label(game, text="DMG", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
dmg_label_1.grid(row=1, column=1)
str_label_1 = tkinter.Label(game, text="STR", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
str_label_1.grid(row=1, column=2)
stl_label_1 = tkinter.Label(game, text="STL", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
stl_label_1.grid(row=1, column=3)
hp_label_2 = tkinter.Label(game, text="HP", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
hp_label_2.grid(row=1, column=4)
dmg_label_2 = tkinter.Label(game, text="DMG", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
dmg_label_2.grid(row=1, column=5)
str_label_2 = tkinter.Label(game, text="STR", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
str_label_2.grid(row=1, column=6)
stl_label_2 = tkinter.Label(game, text="STL", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
stl_label_2.grid(row=1, column=7)

#player and enemy stat indicators-
player_hp = tkinter.Label(game, text="-", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
player_hp.grid(row=2, column=0)
player_dmg = tkinter.Label(game, text="-", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
player_dmg.grid(row=2, column=1)
player_str = tkinter.Label(game, text="-", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
player_str.grid(row=2, column=2)
player_stl = tkinter.Label(game, text="-", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
player_stl.grid(row=2, column=3)
enemy_hp = tkinter.Label(game, text="-", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
enemy_hp.grid(row=2, column=4)
enemy_dmg = tkinter.Label(game, text="-", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
enemy_dmg.grid(row=2, column=5)
enemy_str = tkinter.Label(game, text="-", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
enemy_str.grid(row=2, column=6)
enemy_stl = tkinter.Label(game, text="-", width=5, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
enemy_stl.grid(row=2, column=7)

#Where actions will be displayed
action_display = tkinter.Label(game, text="", height=2, width=60, font=('Helvetica bold',10))
action_display.grid(row=3, column=0, columnspan=8)

#Action buttons
attack_button = tkinter.Button(game, text="Attack", width=15, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=player_attack)
attack_button.grid(row=4, column=0, columnspan=2)
heal_button = tkinter.Button(game, text="Heal", width=15, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=potion_used)
heal_button.grid(row=4, column=2, columnspan=2)
item1_button = tkinter.Button(game, text="Steroid", width=15, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=steroid_used)
item1_button.grid(row=4, column=4, columnspan=2)
item2_button = tkinter.Button(game, text="Invisibility Cloak", width=15, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=invis_used)
item2_button.grid(row=4, column=6, columnspan=2)

loser_label = tkinter.Label(game, text="You Lost", width=15, height=2, font=('Helvetica bold',20))
exit_loser = tkinter.Button(game, text="Exit", width=15, height=2, font=('Helvetica bold',10), command=game.destroy, borderwidth=1, relief="groove")
enemy_defeat = tkinter.Label(game, text=f"You defeated {enemy_1.name}", width=30, height=2, font=('Helvetica bold',20))
new_enemy_button = tkinter.Button(game, text="New Enemy", width=15, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", command=new_enemy)
exit_win = tkinter.Button(game, text="Exit", width=15, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", command=game.destroy)


#Startup Screen



start_screen = tkinter.Tk()
start_screen.title("Start Battle Game")
username_input = tkinter.Entry(start_screen, text="Input Username Here", width=15, font=('Helvetica bold',15), borderwidth=1, relief="solid")
username_input.grid(row=0, column=1, columnspan=3)
spacer1 = tkinter.Label(start_screen, text="")
spacer1.grid(row=1)
easy_select = tkinter.Button(start_screen, text="Easy", width=5, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=easy_chosen)
easy_select.grid(row=2, column=0)
normal_select = tkinter.Button(start_screen, text="Normal", width=5, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=normal_chosen)
normal_select.grid(row=2, column=2)
hard_select = tkinter.Button(start_screen, text="Hard", width=5, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=hard_chosen)
hard_select.grid(row=2, column=4)
spacer2 = spacer1
spacer2.grid(row=3)
warrior_select = tkinter.Button(start_screen, text="Warrior", width=5, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=warrior_chosen)
ranger_select = tkinter.Button(start_screen, text="Ranger", width=5, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=ranger_chosen)
spacer3 = spacer1
spacer3.grid(row=5)
begin_button = tkinter.Button(start_screen, text="Begin", width=5, height=2, font=('Helvetica bold',10), borderwidth=1, relief="groove", state=NORMAL, command=set_up_game)



if __name__ == "__main__":
    game.mainloop()

