# Created By: Brianna Baldwin
import random
import string
from hangman import hangman_words
from root import main


def get_valid_word(word_list):
    word = random.choice(word_list)  # randomly chooses something from list
    while '-' in word or ' ' in word:
        word = random.choice(word_list)

    return word.upper()


def hangman(word_list):
    word = get_valid_word(word_list)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # letters from english dictionary
    used_letters = set()  # letters user guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'c', 'd']) --> 'a b c d'
        print('You have', lives, ' lives left\n'\
                                 'You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in word\n')

        elif user_letter in used_letters:
            print('You have already guessed that letter. Please enter a new letter.\n')

        else:
            print('Invalid character. Please enter a letter\n')

    # if all letters guess or they lose
    if lives == 0:
        print('You died :( The word was ', word)
    print('You guessed the word', word, '!')


def playhangman():
    hangman(hangman_words.words_list)
    playagain()


def restart():
    main.runmenu()


def playagain():
    e = input('To play again enter "r" To go back to menu enter "m"\n').lower()
    if e == "m":
        restart()

    elif e == "r":
        playhangman()

    else:
        print('Invalid entry. Please try again\n')
        playagain()
