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
    def __init__(self,health,strength,defence,mana,speed,spells=[],effects=[]):
        self.health = health
        self.strength = strength
        self.defence = defence
        self.mana = mana
        self.speed = speed
        self.spells = spells
        self.effects = effects
        
    def heal_plus(self,amount):
        self.health += amount

    def damage_plus(self,amount):
        self.health -= amount

    def defend_plus(self,amount):
        self.defence += amount

    def mana_plus(self,amount):
        self.mana += amount

    def speed_plus(self,amount):
        self.speed += amount

    def process_effects(self):
        
        effects_remove = []
        
        for effect in self.effects:
            effect.apply_effect(self)
            
            effect.duration -= 1
         
            if effect.duration <= 0:
                effects_remove.append(effect)
                print(f'{effect.name} has worn off')

        for effect in effects_remove:
            self.effects.remove(effect)
   
    def add_effect(self,effect):
        self.effects.append(effect)
        print(f'{effect.name} has been applied and will last {effect.duration} turns')

    def damage_increase(self,amount):
        self.strength += amount

    def health_increase(self,amount):
        self.health += amount

    def defence_increase(self,amount):
        self.defence += amount

class Spell():
    def __init__(self,name,mana_cost,damage=None,heal=None,speed_increase=None,damage_increase=None,health_increase=None,defence_increase=None,poison=None,burn=None,freeze=None):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.heal = heal
        self.speed_increase = speed_increase
        self.damage_increase = damage_increase
        self.health_increase = health_increase
        self.defence_increase = defence_increase
        self.poison = poison
        self.burn = burn
        self.freeze = freeze

    def mana_cost(self,amount):
        pass

    def speed_increase(self,amount):
        pass

    def damage_increase(self,amount):
        pass

    def heal_increase(self,amount):
        pass

    def wisdom_increase(self,amount):
        pass

    def poison_increase(self,amount):
        pass

    def burn_increase(self,amount):
        pass

    def freeze_increase(self,amount):
        pass

    def health_increase(self,amount):
        pass

    def speed_increase(self,amount):
        pass

    def damage_increase(self,amount):
        pass

    def wisdom_increase(self,amount):
        pass

class Effect():
    def __init__(self, id, name, duration, effect_type="damage", value=0):
        self.id = id
        self.name = name
        self.duration = duration
        self.effect_type = effect_type  
        self.value = value  
        
    def apply_effect(self, character):
        print(f"DEBUG: Applying {self.name} effect (type: {self.effect_type}, value: {self.value}) to {character.__class__.__name__}")
        
        # Check if value is None or 0
        if self.value is None or self.value == 0:
            print(f"DEBUG: {self.name} effect has no value ({self.value}), skipping...")
            return
        
        if self.effect_type == "damage":
            character.damage_plus(self.value)
            print(f"{self.name} deals {self.value} damage!")
        elif self.effect_type == "heal":
            character.heal_plus(self.value)
            print(f"{self.name} heals for {self.value} health!")
        elif self.effect_type == "poison":
            character.damage_plus(self.value)
            print(f"{self.name} poisons for {self.value} damage!")
        elif self.effect_type == "burn":
            character.damage_plus(self.value)
            print(f"{self.name} burns for {self.value} damage!")
        elif self.effect_type == "freeze":
            character.speed_plus(-self.value)  # Reduce speed
            print(f"{self.name} slows you down by {self.value} speed!")
        elif self.effect_type == "strength_buff":
            character.strength += self.value
            print(f"{self.name} increases strength by {self.value}!")
        elif self.effect_type == "defence_buff":
            character.defend_plus(self.value)
            print(f"{self.name} increases defence by {self.value}!")
        elif self.effect_type == "mana_buff":
            character.mana_plus(self.value)
            print(f"{self.name} restores {self.value} mana!")
        else:
            print(f"DEBUG: Unknown effect type: {self.effect_type}")

# class Combat_Section():
#     def __init__(self,)

