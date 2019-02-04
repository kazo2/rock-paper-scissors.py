import random
import time

rps = ['rock','paper','scissors']

def game():
    print('\nChoose rock, paper, or scissors.')
    choice = input().lower()

    if choice in rps:
        AI_choice = random.choice(rps)
        print(f'You chose {choice} and I chose {AI_choice}')
        time.sleep(1)
        if choice == 'rock':
            if AI_choice == 'rock':
                print("Rats! It's a tie.")
                game()
            elif AI_choice == 'paper':
                print("Woo-hoo! Looks like I won.")
            else:
                print("Well played, looks like you won.")

        elif choice == 'paper':
            if AI_choice == 'rock':
                print("Woo-hoo! Looks like I won.")
            elif AI_choice == 'paper':
                print("Rats! It's a tie.")
                game()
            else:
                print("Well played, looks like you won.")
        else:
            if AI_choice == 'rock':
                print("Woo-hoo! Looks like I won.")
            elif AI_choice == 'paper':
                print("Well played, looks like you won.")
            else:
                print("Rats! It's a tie.")
                game()
        time.sleep(2)
        print('\nThat was fun! Wanna play again?\nY/N')
        while True:
            playAgain = input().lower()
            if playAgain not in ('y','yes','sure','ok','okay'):
                break
            game()
    else:
        print('\n' * 15 + 'Please type in either rock, paper, or scissors.')
        game()
game()
