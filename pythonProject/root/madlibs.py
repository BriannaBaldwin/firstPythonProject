# Madlibs minigame
# Created By: Brianna Baldwin

import main
from madlibs_book import harrypotter, lotr, dragon, starwars
import random


def madlibgame():
    print('\nPlaying: Madlibs')
    m = random.choice([harrypotter, lotr, dragon, starwars])
    m.madlib()
    playagain()


def restart():
    main.runmenu()


def playagain():
    e = input('To play again enter "r" To go back to menu enter "m"\n').lower()
    if e == "m":
        restart()

    elif e == "r":
        madlibgame()

    else:
        print('Invalid entry. Please try again\n')
        playagain()
