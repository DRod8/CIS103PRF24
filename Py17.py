import random

def powerball():
    numbers = set()
    while len(numbers) < 5:
        num = random.randint(1, 69)
        if num not in numbers:
            numbers.add(num)
    return sorted(numbers)

def mega_million():
    numbers = set()
    while len(numbers) < 5:
        num = random.randint(1, 70)
        if num not in numbers:
            numbers.add(num)
    return sorted(numbers)

def lucky_day_lotto():
    numbers = set()
    while len(numbers) < 5:
        num = random.randint(1, 45)
        if num not in numbers: 
            numbers.add(num)
    return sorted(numbers)

def lotto():
    numbers = set()
    while len(numbers) < 6:
        num = random.randint(1, 52)
        if num not in numbers:
            numbers.add(num)
    return sorted(numbers)

def show_menu():
    print("\nIllinois Lottery Number Generator:")
    print("1. Powerball")
    print("2. Mega Million")
    print("3. Lucky Day Lotto")
    print("4. Lotto")
    print("9. Quit")

def main():
    choice = "1"
    while choice != '9':
        show_menu()
        choice = input('Please choose a lottery game (1-4) or 9 to Quit:')

        if choice == '1':
            numbers = powerball()
            print(f'Powerball: {", ".join(map(str, numbers))}')
        elif choice == '2':
            numbers = mega_million()
            print(f'Mega Million: {", ".join(map(str, numbers))}')
        elif choice == '3':
            numbers = lucky_day_lotto()
            print(f'Lucky Day Lotto: {", ".join(map(str, numbers))}')
        elif choice == '4':
            numbers = lotto()
            print(f'Lotto: {", ".join(map(str, numbers))}')
        elif choice == '9':
            print('Thank you for using the Illinois Lottery Number Generator. Goodbye.')
            break
        else:
            print('Invalid selection. Please choose a valid option.')
            input('\nPress Enter to return to the menu.')

if __name__ == "__main__":
    main()
