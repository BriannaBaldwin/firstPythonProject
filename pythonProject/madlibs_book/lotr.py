# Superhero madlib
# Created by: Brianna Baldwin
# Created date: 04/25/2022

def madlib():
    print('Lord of the Rings Madlib')
    noun = input('Noun: ').capitalize()
    adjective = input('Adjective: ').lower()
    animal = input('Animal (plural): ').capitalize()
    animal2 = input('Animal (plural): ').capitalize()
    verb = input('Verb (ending in "ing"): ').lower()
    adjective2 = input('Adjective: ').capitalize()
    famous_person = input('Famous person: ').title()
    color = input('Color: ').capitalize()
    noun2 = input('Noun (plural): ').capitalize()
    noun3 = input('Noun (plural): ').lower()
    animal3 = input('Animal (plural): ').lower()
    verb2 = input('Verb (ending in "ed"): ').lower()
    noun4 = input('Noun (plural): ').lower()

    story = f'In J.R.R. Tolkien\'s famous trilogy Lord of the {noun}s, the\n' \
            f'first book is called Fellowship of the {noun}. In this book\n' \
            f'a group of {adjective} Hobbits flee their hometown. They\n' \
            f'eventually join into a fellowship made up of {animal}, ' \
            f'Elves and {animal2}, with the goal of {verb}\n' \
            f'the One {noun}. They begin by traveling through the\n' \
            f'{adjective2} Mountains, where {famous_person} the\n' \
            f'{color} is lost. They continue on to the forest, where the\n' \
            f'queen of the {noun2} gives them {noun3} to\n' \
            f'ride down the river. At the end of the book, Merry and Pippin get\n' \
            f'captured by {animal3}, and Frodo is {verb2} by one of his\n' \
            f'fellow {noun4} and leaves on his own (but with Sam).\n'

    print(story)
