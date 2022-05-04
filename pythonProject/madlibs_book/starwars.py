# Superhero madlib
# Created by: Brianna Baldwin
# Created date: 04/25/2022

def madlib():
    print('Star Wars Madlib')
    name = input('Name: ').capitalize()
    adjective = input('Adjective: ').lower()
    verb = input('Verb: ').lower()
    silly_word = input('Silly word: ').capitalize()
    noun = input('Noun: ').lower()
    noun2 = input('Noun (plural): ').lower()
    verb2 = input('Verb (ending in "ed"): ').lower()
    noun3 = input('Noun: ').lower()
    noun4 = input('Noun: ').lower()
    verb3 = input('Verb (ending in "ed"): ').lower()
    adjective2 = input('Adjective: ').lower()

    story = f'Darth {name} looked at his masteer while his\n' \
            f'{adjective} breathing filled the room. He was told to go\n' \
            f'{verb} everything on the planet of {silly_word}.\n' \
            f'He got in his {noun} and jumped to hyperspace. Soon\n' \
            f'before he reached the planet, he dropped out of hyperspace and was\n' \
            f'attacked by Rebel {noun2}. He {verb2} them\n' \
            f'off and continued to the planet\'s surface. He landed and confronted more\n' \
            f'opposition, slicing it down with his {noun3}. He used the\n' \
            f'{noun4} to choke another Rebel, then {verb3}\n' \
            f'him aside. He finished off all life on the planet with a/an\n' \
            f'{adjective2} laugh.\n'

    print(story)
