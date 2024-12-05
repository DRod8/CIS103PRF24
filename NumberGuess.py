import random

def clear_screen():
    print("\n" * 20)

def get_valid_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = input(prompt).strip()
            if value == "":
                return None
            value = int(value)
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                raise ValueError(f"Please enter a number between {min_value} and {max_value}.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def play_game(player_name):
    clear_screen()
    n = random.randint(1, 200)
    default_chances = 15

    chances = get_valid_integer("Enter the number of chances (1-100, press Enter for default 15): ", 1, 100)
    if chances is None:
        chances = default_chances

    guesses_made = 0
    error_guesses = 0
    good_guesses = 0

    while guesses_made < chances:
        print(f"\nChances left: {chances - guesses_made}")
        guess = get_valid_integer("Enter an integer from 1 to 200: ", 1, 200)

        if guess is None:
            error_guesses += 1
            print("Invalid input. Please try again.")
            continue

        guesses_made += 1
        good_guesses += 1

        if guess < n:
            print("Your guess is too low.")
        elif guess > n:
            print("Your guess is too high.")
        else:
            print(f"Congratulations {player_name}, you guessed it!")
            break
    else:
        print(f"Sorry {player_name}, you've run out of chances. The number was {n}.")

    print(f"\nGame Over! You made {good_guesses} valid guesses and {error_guesses} invalid attempts.")

def main():
    player_name = input("Enter your name: ").strip()
    while True:
        play_game(player_name)
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    
  
  main()
