import sys
from classes import *
from combat import *

def main(story):
    print(story.worldbuilding)
    choice = input(story.question)
    try:
        selected_choice = None
        for choice_obj in story.choices:
            if choice_obj.id.lower() == choice.lower():
                selected_choice = choice_obj
                break
        
        if selected_choice:
            print(selected_choice.description)
            # If there's a next section, continue the story
            if selected_choice.next_section:
                if selected_choice.next_section == "combat":
                    # Start combat with the cultist
                    combat_section(player1, enemy_cultist)
                else:
                    main(selected_choice.next_section)
            if selected_choice.end_game:
                sys.exit(0)
        else:
            valid_choices = [choice_obj.id for choice_obj in story.choices]
            raise ValueError(f"Invalid choice: '{choice}'. Please enter one of: {', '.join(valid_choices)}")
    except ValueError as e:
        print(e)
        main(story)



# Create story sections first
story1 = Story_Section('Start',
'You walk down a long path that seems to en in a cross section.. o you want to go to the left , right or straight across',
'Enter your choice (left, right, straight): ',
[])

story2 = Story_Section('Dog',
'You encounter the dog and notice it is very large and aggressive',
'What do you do? (ignore, pet, run)',
[])

story3 = Story_Section('Market',
'You see a market dead ahead with lots of people',
'What do you do? (go to the market), ignore the market and walk past , go to the market and talk to the people (look, pass, talk))',
[])

story4 = Story_Section('Alley',
'You go down and can barely make out the silhouette of a hooded figure , who seems to disappear down a side alley',
'What do you do?' 'Alley, Ignore the alley and walk past, Go to the alley and talk to the people)(follow, ignore , introduce))',
[])

story5 = Story_Section('End',
'You follow the hooded figure down the alley and introduce yourself. The figure then promptly kills you',
'You died , would you like to play again? (yes, no)',
[])

# Create choices with None as next_section initially
Choice1 = Choice('left', 'You encounter a dog', None)
Choice2 = Choice('right', 'You see a market dead ahead with lots of people', None)
Choice3 = Choice('straight', 'Nothing interesting happens, but you notice an alley peeking out from the right', None)

Choice4 = Choice('ignore', 'The dog barks at you and runs away', None)
Choice5 = Choice('pet', 'The dog wags its tail and wags its tail', None)
Choice6 = Choice('run', 'The dog chases you and you fall down', None)

Choice7 = Choice('look', 'You go to the market look around for a while', None)
Choice8 = Choice('pass', 'You ignore the market and walk past', None)
Choice9 = Choice('talk', 'You go to the market and talk to the people', None)

Choice10 = Choice('follow', 'You follow the hooded figure down the alley and wait behind a corner', None)
Choice11 = Choice('ignore', '(BORING) You ignore the alley and walk past', None)
Choice12 = Choice('introduce', 'You follow the hooded figure down the alley and introducee yourself like an idiot', None)
Choice13 = Choice('yes', 'You play again', story1, True)
Choice14 = Choice('no', 'You exit the game', None)
# Now update the story sections with their choices
story1.choices = [Choice1, Choice2, Choice3]
story2.choices = [Choice4, Choice5, Choice6]
story3.choices = [Choice7, Choice8, Choice9]
story4.choices = [Choice10, Choice11, Choice12]
story5.choices = [Choice13, Choice14]
# Finally, update the choices with their next_section references
Choice1.next_section = story2  #DOG story
Choice2.next_section = story3  #MARKET story
Choice3.next_section = story4  #ALLEY story
Choice12.next_section = "combat" 


story = []


if __name__ == '__main__':
    main(story1)



