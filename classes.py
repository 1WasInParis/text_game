class Choice:
    def __init__(self, id, description, next_section=None,end_game=None,action=None):
        self.id = id
        self.description = description
        self.next_section = next_section
        self.end_game = end_game
        self.action = action

class Story_Section:
    def __init__(self, id, worldbuilding, question, choices,):
        self.id = id
        self.worldbuilding = worldbuilding
        self.question = question
        self.choices = choices

class Character():
    def __init__(self,health,strength,defence):
        self.health = health
        self.strength = strength
        self.defence = defence
    def heal_plus(self,amount):
        self.health += amount

    def damage_plus(self,amount):
        self.health -= amount

    def defend_plus(self,amount):
        self.defence += amount


# class Combat_Section():
#     def __init__(self,)

