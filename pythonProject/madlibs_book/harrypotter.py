# Harry Potter madlib
# Created by: Brianna Baldwin
# Created date: 04/25/2022

def madlib():
    print('Harry Potter Madlib')
    noun1 = input('Plural noun: ').capitalize()
    famous_person = input('Famous person: ').title()
    mythical_creature = input('Mythical creature: ').lower()
    noun2 = input('Noun: ').lower()
    verb1 = input('Verb: ').lower()
    verb2 = input('Verb (ending in "ed"): ').lower()
    famous_person2 = input('Famous person: ').title()
    verb3 = input('Verb (ending in "ed"): ').lower()
    adjective1 = input('Adjective: ').lower()
    noun3 = input('Plural noun: ').lower()
    famous_person3 = input('Famous person: ').title()
    occupation1 = input('Occupation: ').lower()
    adjective2 = input('Adjective: ').capitalize()
    adverb = input('Adverb (ending in "ly"): ').lower()
    material = input('Material: ').lower()
    occupation2 = input('Occupation: ').capitalize()
    adjective3 = input('Adjective: ').lower()

    story = f'In his second term at Hogwarts School of {noun1} and\n \
            Wizardry, Harry Potter ({famous_person}) is warned by a/an \n \
            {mythical_creature} named Dobby that {noun2} will\n \
            {verb1} when he returns to Hogwarts. Besides the fact that he\n \
            is still {verb2} by Professor Snape ({famous_person2})\n \
            and {verb3} by Draco Malfoy (Tom Felton), Harry gets off to\n \
            a {adjective1} start with his two best {noun3}, Ron\n \
            Weasly (Rupert Grint) and Hermione Granger ({famous_person3}).\n \
            Also, famous {occupation1} Gilderoy Lockhart (Kenneth Branagh)\n \
            has joined the Hogwarts staff and is the new Defense Against the\n \
            {adjective2} Arts teacher. But now, Hogwarts students are\n \
            {adverb} being turned into {material}. But who is\n \
            the one doing it? Malfoy? {occupation2} Hagrid (Robbie Coltrane)?\n \
            Or even Harry? But what if it\'s Lord Voldemort trying to make his\n \
            {adjective3} return?\n'

    print(story)
