# Rock Paper Scissors game
# Created By: Brianna Baldwin
import random
from root import main


def play():
    print("\nPlaying: Rock Paper Scissors")
    user = input('What\'s your choice?: "r" for rock, "p" for paper, "s" for scissors\n').lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie\n'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!\n'

    if is_win(computer, user):
        return 'You lost :(\n'

    else:
        print('Invalid entry. Please try again.\n')
        playrpc()


def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


def playrpc():
    print(play())
    playagain()


def restart():
    main.runmenu()


def playagain():
    e = input('To play again enter "r" To go back to menu enter "m"\n').lower()
    if e == "m":
        restart()

    elif e == "r":
        playrpc()

    else:
        print('Invalid entry. Please try again.\n')
        playagain()
