from classes import *

player1 = Character(100,10,1)
enemy1 = Character(50,5,1)


def combat_section(player,enemy):
    print("You are facing an enemy")
    print("You can choose to attack or heal or defend")
    combat_choice = input('what would you like to do(attack, heal, defend)')
    
    # Player's turn
    if combat_choice == 'attack':
        enemy.damage_plus(player.strength/enemy.defence)
        print(f"You attack the enemy for {player.strength/enemy.defence} damage!")
    elif combat_choice == 'heal':
        player.heal_plus(10)
        print("You heal yourself for 10 health!")
    elif combat_choice == 'defend':
        player.defend_plus(1)
        print("You take a defensive stance!")

    # Check if enemy died from player's attack
    if enemy.health <= 0:
        print("You have defeated the enemy!")
        return  # Exit combat, don't let dead enemy attack
    
    # Enemy's turn (only if enemy is still alive)
    print(f'The enemy has {enemy.health} health left')
    print(f'The enemy attacks you, dealing {enemy.strength/player.defence} damage')
    player.damage_plus(enemy.strength/player.defence)
    print(f'You have {player.health} health left')
    
    # Check if player died from enemy's attack
    if player.health <= 0:
        print("You have died!")
        return  # Exit combat
    
    # Continue combat if both are alive
    combat_section(player,enemy)

if __name__ == '__main__':
    combat_section(player1,enemy1)
       