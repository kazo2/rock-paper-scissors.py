import random
import time


def game():
    print('\nChoose rock, paper, or scissors.')
    choice = input().lower()

    if choice in ['rock', 'paper', 'scissors']:
        AI_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f'You chose {choice} and I chose {AI_choice}')
        time.sleep(1)
        if choice == 'rock' and AI_choice == 'scissors' or choice == 'paper' and AI_choice == 'rock' or choice == 'scissors' and AI_choice == 'paper':
            print("Well played, looks like you won.")
            time.sleep(2)
        elif choice == 'paper' and AI_choice == 'scissors' or choice == 'scissors' and AI_choice == 'rock' or choice == 'rock' and AI_choice == 'paper':
            print("Woo-hoo! Looks like I won.")
            time.sleep(2)
        elif choice == 'scissors' and AI_choice == 'scissors' or choice == 'rock' and AI_choice == 'rock' or choice == 'paper' and AI_choice == 'paper':
            print("Rats! It's a tie.")
            time.sleep(2)
        print('\nThat was fun! Wanna play again?\nY/N')
        while True:
            playAgain = input().lower()
            if playAgain not in ('y', 'yes', 'sure', 'ok', 'okay'):
                break
            game()
    else:
        print('\nPlease type in either rock, paper, or scissors.')
        time.sleep(1)
        game()


game()
