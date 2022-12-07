#Player data {difficulty: [health, damage]}
person_hp = {'easy' : [150, 25],
               'normal' : [100, 20],
               'hard' : [50, 15]}

#Main player class with username and difficulty
class Person:
    difficulty_list = ['easy', 'normal', 'hard']
    def __init__(self, username = 'Player 1', difficulty = "normal"):
        self.username = username
        self.difficulty = difficulty
        #assigns stats based on difficulty chosen by the player
        try:
            if difficulty.lower() in self.difficulty_list:
                if difficulty == 'easy':
                    self.health = (person_hp['easy'])[0]
                    self.damage = (person_hp['easy'])[1]
                elif difficulty == 'hard':
                    self.health = (person_hp['hard'])[0]
                    self.damage = (person_hp['hard'])[1]
                else:
                    self.health = (person_hp['normal'])[0]
                    self.damage = (person_hp['normal'])[1]
            else:
                raise Not_Valid_Difficulty()
        except:
            raise Not_Valid_Difficulty()



    def __str__(self):
        return f"Username: {self.username}\n" \
               f"Chosen Difficulty: {self.difficulty.upper()}"

    def __repr__(self):
        return f"Username: {self.username}\n" \
               f"Chosen Difficulty: {self.difficulty.upper()}"


class Not_Valid_Difficulty(Exception):
    '''Not a valid difficulty'''
    pass


