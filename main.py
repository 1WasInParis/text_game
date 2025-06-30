def main(story):
    print(story.worldbuilding)
    choice = input(story.question)
    try:
        selected_choice = None
        for choice_obj in story.choices:
            if choice_obj.id == choice:
                selected_choice = choice_obj
                break
        
        if selected_choice:
            print(selected_choice.description)
            # If there's a next section, continue the story
            if selected_choice.next_section:
                main(selected_choice.next_section)
        else:
            valid_choices = [choice_obj.id for choice_obj in story.choices]
            raise ValueError(f"Invalid choice: '{choice}'. Please enter one of: {', '.join(valid_choices)}")
    except ValueError as e:
        print(e)
        main(story)


class Choice:
    def __init__(self, id, description, next_section=None):
        self.id = id
        self.description = description
        self.next_section = next_section

class Story_Section:
    def __init__(self, id, worldbuilding, question, choices):
        self.id = id
        self.worldbuilding = worldbuilding
        self.question = question
        self.choices = choices

# Create story sections first
story1 = Story_Section('Start',
'You walk down a long path that seems to en in a cross section.. o you want to go to the left , right or straight across',
'Enter your choice (left, right, straight): ',
[])

story2 = Story_Section('Dog',
'You encounter the dog and notice it is very large and aggressive',
'What do you do? (Ignore, Pet, Run)',
[])

# Create choices with None as next_section initially
Choice1 = Choice('left', 'You encounter a dog', None)
Choice2 = Choice('right', 'You see a market dead ahead with lots of people', None)
Choice3 = Choice('straight', 'Nothing interesting happens, but you notice an alley peeking out from the right', None)

Choice4 = Choice('Ignore', 'The dog barks at you and runs away', None)
Choice5 = Choice('Pet', 'The dog wags its tail and wags its tail', None)
Choice6 = Choice('Run', 'The dog chases you and you fall down', None)

Choice7

# Now update the story sections with their choices
story1.choices = [Choice1, Choice2, Choice3]
story2.choices = [Choice4, Choice5, Choice6]

# Finally, update the choices with their next_section references
Choice1.next_section = story2
Choice2.next_section = story2  # You can change this to story3 when you create it
Choice3.next_section = story2  # You can change this to story4 when you create it














story = []


if __name__ == '__main__':
    main(story1)



