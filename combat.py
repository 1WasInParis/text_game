from classes import *

player1 = Character(100,10,1,100,12)
enemy_cultist = Character(50,5,1,0,10)



# Create more spells
# name , mana_cost , damage , heal , speed_increase , damage_increase , health_increase , defence_increase , poison , burn , freeze
fireball = Spell("Fireball", -25, 25, 0, 0, 0, 0, 0, 0, 10, 0)
heal = Spell("Heal", -10, 0, 10, 0, 0, 0, 0, 0, 0, 0)
speed = Spell("Speed", -10, 0, 0, 10, 0, 0, 0, 0, 0, 0)
poison = Spell("Poison", -15, 5, 0, 0, 0, 0, 0, 10, 0, 0)
ice_shard = Spell("Ice Shard", -10, 15, 0, 0, 0, 0, 0, 0, 0, 10)
shield = Spell("Shield", -10, 0, 0, 0, 0, 0, 9, 0, 0, 0)
lightning = Spell("Lightning", -35, 40, 0, 0, 0, 0, 0, 0, 0, 0)

# Create some example effects using the actual spell values
poison_effect = Effect("poison_1", "Poison", 3, "poison", poison.poison)
burn_effect = Effect("burn_1", "Burn", 2, "burn", 8)  # Use fixed value since fireball.burn is 0
freeze_effect = Effect("freeze_1", "Freeze", 2, "freeze", ice_shard.freeze)
strength_buff = Effect("strength_1", "Strength Potion", 2, "strength_buff", 5)
speed_buff = Effect("speed_1", "Speed Potion", 2, "speed_buff", speed.speed_increase)

# Give player some starting spells
player1.spells.append(fireball)
player1.spells.append(heal)
player1.spells.append(speed)
player1.spells.append(poison)
player1.spells.append(ice_shard)
player1.spells.append(shield)
player1.spells.append(lightning)

# Function to get available spell names
def get_available_spells(player):
    return [spell.name for spell in player.spells]

# Function to find a spell by name
def find_spell(player, spell_name):
    for spell in player.spells:
        if spell.name == spell_name:
            return spell
    return None

print("You are facing an enemy")

def combat_section(player,enemy): 
    if player.speed > enemy.speed:
        player_turn(player,enemy)
        enemy_turn(player,enemy)
    else:
        enemy_turn(player,enemy)
        player_turn(player,enemy)

    # Process effects on player first
    if len(player.effects) > 0:
        print("\n--- Player Effects Processing ---")
        player.process_effects()
        print(f'Player has {len(player.effects)} effects after processing: {[e.name for e in player.effects]}')
        print("--- End Player Effects ---\n")
    
    # Process effects on enemy (poison, burn, etc.)
    if len(enemy.effects) > 0:
        print("\n--- Enemy Effects Processing ---")
        enemy.process_effects()
        print(f'Enemy has {len(enemy.effects)} effects after processing: {[e.name for e in enemy.effects]}')
        print("--- End Enemy Effects ---\n")

      # Check if enemy died from player's attack
    if enemy.health <= 0:
        print("You have defeated the enemy!")
        return  # Exit combat, don't let dead enemy attack
    elif enemy.health > 0:
         print(f'The enemy has {enemy.health} health left')

      # Check if player died from enemy's attack
    if player.health <= 0:
        print("You have died!")
        sys.exit(0)
    else:
        print(f'\nYou have {player.health} health left')
        
    if player.mana <= 0:
        print("You have no mana left!")
    else:
        print(f'You have {player.mana} mana left')

    # Continue combat if both are alive
    combat_section(player,enemy)


def player_turn(player,enemy):  
    combat_choice = input('what would you like to do?(attack, defend, magic or nothing)')
    # Player's turn
    try:
        if combat_choice == 'attack':
            enemy.damage_plus(player.strength/enemy.defence)
            print(f"You attack the enemy for {player.strength/enemy.defence} damage!")
        elif combat_choice == 'defend':
            player.defend_plus(1)
            print("You take a defensive stance!")
        elif combat_choice == 'magic':
            available_spells = get_available_spells(player)
            if not available_spells:
                print("You don't know any spells!")
                return
            print(f"\nAvailable spells: {', '.join(available_spells)}")
            magic_choice = input(f'\nWhich spell would you like to cast? ({", ".join(available_spells)}): ')
            try:
                spell = find_spell(player, magic_choice)
                if spell:
                    if player.mana >= abs(spell.mana_cost):
                        player.mana_plus(spell.mana_cost)
                        
                        # Apply all spell effects (not just the first one)
                        if spell.damage:
                            enemy.damage_plus(spell.damage)
                            print(f"\nYou cast {spell.name} at the enemy for {spell.damage} damage!")
                        
                        if spell.heal:
                            # Create a new heal effect instance for the player
                            player_heal_effect = Effect("heal_1", "Regeneration", 3, "heal", spell.heal)
                            player.add_effect(player_heal_effect)
                            print(f'\nYou cast {spell.name} and heal for {spell.heal} health!')
                            print(f'DEBUG: Player now has {len(player.effects)} effects: {[e.name for e in player.effects]}')
                            print(f'DEBUG: Enemy has {len(enemy.effects)} effects: {[e.name for e in enemy.effects]}')
                        
                        if spell.speed_increase:
                            player.add_effect(speed_buff)
                            print(f'\nYou cast {spell.name} and increase your speed by {spell.speed_increase}!')
                        
                        if spell.damage_increase:
                            player.damage_increase(spell.damage_increase)
                            print(f'\nYou cast {spell.name} and increase your damage by {spell.damage_increase}!')
                        
                        if spell.health_increase:
                            player.health_increase(spell.health_increase)
                            print(f'\nYou cast {spell.name} and increase your health by {spell.health_increase}!')
                        
                        if spell.defence_increase:
                            player.defence_increase(spell.defence_increase)
                            print(f'\nYou cast {spell.name} and increase your defence by {spell.defence_increase}!')
                        
                        if spell.poison:
                            enemy.add_effect(poison_effect)  # Add poison effect to enemy
                            print(f"Poison effect value: {poison_effect.value}")
                            print(f'\nYou cast {spell.name} and poison for {spell.poison}!')
                            print(f'Enemy now has {len(enemy.effects)} effects: {[e.name for e in enemy.effects]}')
                        
                        if spell.burn:
                            enemy.add_effect(burn_effect)  # Add burn effect to enemy
                            print(f'\nYou cast {spell.name} and burn for {spell.burn}!')
                            print(f'Enemy now has {len(enemy.effects)} effects: {[e.name for e in enemy.effects]}')
                        
                        if spell.freeze:
                            enemy.add_effect(freeze_effect)
                            print(f'\nYou cast {spell.name} and freeze for {spell.freeze}!')
                            print(f'Enemy now has {len(enemy.effects)} effects: {[e.name for e in enemy.effects]}')
                    else:
                        print(f"Not enough mana! You need {abs(spell.mana_cost)} mana but have {player.mana}")
                else:
                    print(f"Unknown spell: {magic_choice}")
                    return
            except ValueError as e:
                print(e)
                player_turn(player,enemy)
        elif combat_choice == 'nothing':
            print("You do nothing")
        else:
            valid_combat_choices = ['attack','defend','heal','magic','nothing']
            raise ValueError(f"Invalid choice: '{combat_choice}'. Please enter one of: {', '.join(valid_combat_choices)}")
    except ValueError as e:
        print(e)
        player_turn(player,enemy)


def enemy_turn(player,enemy):
    print(f'The enemy attacks you, dealing {enemy.strength/player.defence} damage')
    player.damage_plus(enemy.strength/player.defence)


if __name__ == '__main__':
    combat_section(player1,enemy1)

