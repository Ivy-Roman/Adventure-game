import time
import random
import string

words = ['wicked fairie', 'dragon', 'troll', 'dinosaur']
random_choice = random.choice(words)


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.25)
        time.sleep(.03)
    print('')


def print_pause(message, delay=1):
    typewriter_simulator(message)
    time.sleep(delay)


def intro():
    lines = ['You find yourself standing in an open field',
             'filled with grass and yellow wildflowers.',
             f'Rumor has it that a {random_choice}' +
             ' is somewhere around here,' +
             ' and has been terrifying the nearby village.',
             'In front of you is a house.',
             'To your right is a dark cave.',
             'In your hand you hold your trusty (but not very effective)' +
             ' dagger.']

    for line in lines:
        print_pause(line)


def valid_input(prompt, options):
    while True:
        option = input(prompt)
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def runaway(items):
    print_pause('You run back into the field. Luckily,' +
                ' you don\'t seem to have been followed.\n')
    print_pause('However, he who fights and runs away lives to' +
                ' fight another day.\n')
    options(items)


def play_again():
    third_choice = valid_input('Would you like to play again?' +
                               ' (y/n)\n', ['y', 'n'])
    if third_choice == 'y':
        global random_choice
        random_choice = random.choice(words)
        print_pause('Excellent! Restarting the game ...')
        play_game()
    else:
        print_pause('Thanks for playing! See you next time.')
        exit(0)


def option1(items):
    print_pause('You approach the door of the house.')
    print_pause(f'Eep! This is the {random_choice}\'s house!')
    print_pause(f'The {random_choice} attacks you!')
    if 'magical sword' in items:
        second_choice = valid_input('Would you like to (1) fight' +
                                    ' or (2) run away?\n', ['1', '2'])
        if second_choice == '1':
            print_pause(f'As the {random_choice} moves to attack,' +
                        ' you unsheath your new sword.')
            print_pause('The Sword of Ogoroth shines brightly in' +
                        ' your hand as you brace yourself for the attack.')
            print_pause(f'But the {random_choice} takes one look at your'
                        + ' shiny new toy and runs away!')
            print_pause(f'You have rid the town of the {random_choice}.' +
                        ' You are victorious!\n')
        else:
            runaway(items)
    else:
        print_pause('You feel a bit under-prepared for this,' +
                    ' what with only having a tiny dagger.')
        second_choice = valid_input('Would you like to (1) fight' +
                                    ' or (2) run away?\n', ['1', '2'])
        if second_choice == '1':
            print_pause('You do your best...')
            print_pause('but your dagger is no match for the' +
                        f' {random_choice}.')
            print_pause('You have been defeated!\n')
        else:
            runaway(items)

    play_again()


def option2(items):
    print_pause('You peer cautiously into the cave.')
    if 'magical sword' in items:
        print_pause('You\'ve been here before, and gotten all the good stuff.')
        print_pause('It\'s just an empty cave now.')
        print_pause('You walk back out to the field.\n')
        options(items)
    else:
        print_pause('It turns out to be only a very small cave.')
        print_pause('Your eye catches a glint of metal behind a rock.')
        print_pause('You have found the magical Sword of Ogoroth!')
        print_pause('You discard your silly old dagger' +
                    ' and take the sword with you.')
        print_pause('You walk back out to the field.\n')
        items.append('magical sword')
        options(items)


def options(items):
    print_pause('Enter 1 to knock on the door of the house.')
    print_pause('Enter 2 to peer into the cave.')
    print_pause('What would you like to do?')
    choice = valid_input('(Please enter 1 or 2.)\n', ['1', '2'])
    if choice == '1':
        option1(items)
    else:
        option2(items)


def play_game():
    items = []
    intro()
    options(items)


if __name__ == '__main__':
    play_game()
