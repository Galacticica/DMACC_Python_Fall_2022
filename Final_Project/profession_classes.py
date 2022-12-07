from person_class import Person

#Warrior class (used to affect stats later on)
class Warrior(Person):
    def __init__(self, username = "Player 1", difficulty = "normal", strength = 5, stealth = 2):
        super().__init__(username, difficulty)
        self.strength = strength
        self.stealth = stealth
        
    def __str__(self):
        person_str = super().__str__()
        return f"{person_str}\n" \
               f"Strength: {self.strength}\n" \
               f"Stealth: {self.stealth}"
    
    def __repr__(self):
        person_repr = super().__repr__()
        return f"{person_repr}\n" \
               f"Strength: {self.strength}\n" \
               f"Stealth: {self.stealth}"
        
    

#Same as warrior class but with different strength and stealth
class Ranger(Person):
    def __init__(self, username = "Player 1", difficulty = "normal", strength = 2, stealth = 5):
        super().__init__(username, difficulty)
        self.strength = strength
        self.stealth = stealth
            
    def __str__(self):
        person_str = super().__str__()
        return f"{person_str}\n" \
               f"Strength: {self.strength}\n" \
               f"Stealth: {self.stealth}"
    
    def __repr__(self):
        person_repr = super().__repr__()
        return f"{person_repr}\n" \
               f"Strength: {self.strength}\n" \
               f"Stealth: {self.stealth}"
        
        
