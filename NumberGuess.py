# Dan Rodriguez

import random

def main():
    ch = 1
    while ch == 1:
        name = input('Enter Your Name: ')


        guesses = -1
        while guesses == -1:
            guesses = input('\nEnter Number of Chances: (Between 1-100 or Press ENTER for 15): ')


            if guesses == '':
                guesses = 15
            elif guesses.isdigit():
                guesses = int(guesses)

                if guesses < 1 or guesses > 100:
                    print('Number must be between 1-100!')
                    guesses = -1
            else:
                print('Must be a Number!')
                guesses = -1

        n = random.randint(1, 200)
        guesses_left = guesses
        guesses_used = 0
        error_guesses = 0

        while guesses_left > 0:
            print(f'Guesses Made: {guesses_used}, Guesses Left: {guesses_left}', end=' ')
            guess = -1

            while guess == -1:
                guess = input('Guess the Number: ')

                if guess.isdigit():
                    guess = int(guess)
                    if guess < 1 or guess > 200:
                        print('Number must be between 1-200')
                        guess = -1
                        error_guesses += 1  
                    elif guess < n:
                        print('Number is too LOW!')
                    elif guess > n:
                        print('Number is too HIGH!')
                    else:
                        print(f'Congratulations, {name}! You WON {n}!')
                        break  
                else:
                    print('Please enter a valid number.')
                    error_guesses += 1

            if guess == n:
                break  

            guesses_used += 1
            guesses_left -= 1

        if guesses_left == 0 and guess != n:
            print(f'Sorry, {name}, You LOST! The correct number was {n}.')

        print('Guesses Made: ', guesses_used + error_guesses)
        print('Error Guesses: ', error_guesses)

        while True:
            play_again = input('Play Again? (Y/N): ').strip().lower()
            if play_again == 'Y' or play_again=='y':
                ch = 1
                break
            elif play_again == 'N' or play_again=='n':
                print('Thank You,', name, 'See you Later!')
                ch = 0
                break
            else:
                print("Error: Please enter 'Y' or 'N'!")
        
        print('\n' * 5
              )

if __name__ == "__main__":
    main()
