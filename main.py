import random
import time

def game():
    print('Choose rock, paper, or scissors.')
    choice = input()

    if choice.lower() in ('rock','paper','scissors'):
        AI_choice = random.choice(['Rock','Paper','Scissors'])
        print(f'You chose {choice.lower()} and I chose {AI_choice.lower()}')
        time.sleep(1)
        if choice.lower() == 'rock':
            if AI_choice == 'Rock':
                print("Rats! It's a tie.")
            elif AI_choice == 'Paper':
                print("Woo-hoo! Looks like I won.")
            else:
                print("Well played, looks like you won.")

        elif choice.lower() == 'paper':
            if AI_choice == 'Rock':
                print("Woo-hoo! Looks like I won.")
            elif AI_choice == 'Paper':
                print("Rats! It's a tie.")
            else:
                print("Well played, looks like you won.")
        else:
            if AI_choice == 'Rock':
                print("Woo-hoo! Looks like I won.")
            elif AI_choice == 'Paper':
                print("Well played, looks like you won.")
            else:
                print("Rats! It's a tie.")
        time.sleep(1)
        print('That was fun! Wanna play again?\nY/N')
        playAgain = input()
        if playAgain.lower() in ('y','yes','sure'):
            game()
        else:
            exit()
    else:
        print('Please type in either rock, paper, or scissors.\n')
        time.sleep(1)
        game()
game()
