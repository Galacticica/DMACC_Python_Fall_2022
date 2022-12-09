import random
#defines available enemies {enemy : health, damage, strength, stealth
enemies = {"Slime" : [25, 10, 1, 2],
           "Dragon" : [75, 25, 4, 1],
           "Healer" : [100, 15, 2, 4]}
#updates with each new enemy
class Enemy:
    def __init__(self):
        self.name = "Null"
        self.health = 0
        self.damage = 0
        self.strength = 0
        self.stealth = 0

    def new_enemy(self):
        '''selects a random enemy from the given dictionary above'''
        random_enemy = random.choice(list(enemies.keys()))
        self.name = random_enemy
        self.health = (enemies[random_enemy])[0]
        self.damage = (enemies[random_enemy])[1]
        self.strength = (enemies[random_enemy])[2]
        self.stealth = (enemies[random_enemy])[3]


    def __str__(self):
        return f"{self.name}\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n" \
               f"Strength: {self.strength}\n" \
               f"Stealth: {self.stealth}"

    def __repr__(self):
        return f"{self.name}\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n" \
               f"Strength: {self.strength}\n" \
               f"Stealth: {self.stealth}"



