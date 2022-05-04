# Dragon madlib
# Created by: Brianna Baldwin
# Created date: 04/25/2022

def madlib():
    print('Dragon Madlib')
    color = input('Color: ').lower()
    superlative = input('Superlative (ending in "est"): ').lower()
    adjective = input('Adjective: ').lower()
    body_part = input('Body part (plural): ').lower()
    body_part2 = input('Body part: ').lower()
    noun = input('Noun: ').lower()
    animal = input('Animal (plural): ').lower()
    adjective2 = input('Adjective: ').lower()
    adjective3 = input('Adjective: ').lower()
    adjective4 = input('Adjective: ').lower()

    story = f'The {color} Dragon is the {superlative} dragon of\n ' \
            f'all. It has {adjective} {body_part}, and a {body_part2}\n ' \
            f'shaped like a {noun}. It loves to eat {animal}, although it\n ' \
            f'will feast on nearly anything. It is {adjective2} and {adjective3}.\n ' \
            f'You must be {adjective4} around it, or you may end up as its meal!\n'

    print(story)
