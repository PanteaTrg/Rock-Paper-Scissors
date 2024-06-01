# Version 1: 6/1/2024
import random
import sys
import time

print('Rock, Paper, Scissors, by one and only :) Pantea Tourang')
print()
print('- Rock beats Scissors')
print('- Paper beats Rock')
print('- Scissors beats paper')
print()

wins_count = lost_count = ties_count = 0
items_dict = {'p': 'Paper', 's': 'Scissors', 'r': 'Rock'}

while True:
    print(f'{wins_count} Wins, {lost_count} Losses, {ties_count} Ties')

    # -------------
    # System's move
    # -------------
    system_move = random.choice(list(items_dict.values()))

    # -------------
    # User's move
    # -------------
    print()

    time.sleep(1)
    print('Enter your move: (R)ock (P)aper (S)issors or (Q)uit:')
    user_move = input('>: ').lower()

    print()

    if user_move == 'q':
        print('Thanks for playing, See you soon, Bye :)')
        sys.exit()

    elif user_move not in ('p', 'r', 's'):
        print('Not a valid input! Try Again')

    else:
        user_move = items_dict[user_move]

        print(f'{user_move} versus...')
        print('1...')
        print('2...')
        print('3...')
        print(system_move)

        if user_move == system_move:
            print()
            print("It's a Tie !!")
            ties_count += 1

        elif user_move == 'Rock':
            if system_move == 'Scissors':
                wins_count += 1
                print('You win!')
            elif system_move == 'Paper':
                lost_count += 1
                print('You lose!')

        elif user_move == 'Paper':
            if system_move == 'Rock':
                wins_count += 1
                print('You win!')
            elif system_move == 'Scissors':
                lost_count += 1
                print('You lose')

        elif user_move == 'Scissors':
            if system_move == 'Paper':
                wins_count += 1
                print('You win!')
            elif system_move == 'Rock':
                lost_count += 1
                print('You lose')


