# Created By: Brianna Baldwin
from root import madlibs, hangman_game
from rpc import rock_paper_scissors


def runmenu():
    answer = input('What game would you like to play?\n \
                    Enter "r" to play Rock Paper Scissors\n \
                    Enter "m" to play Madlibs\n \
                    Enter "h" to play Hangman\n').lower()

    if answer == 'm':
        madlibs.madlibgame()

    elif answer == 'r':
        rock_paper_scissors.playrpc()

    elif answer == 'h':
        hangman_game.playhangman()

    else:
        print('Invalid entry. Please try again.\n')
        runmenu()


if __name__ == '__main__':
    runmenu()
