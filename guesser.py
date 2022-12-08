from random import randint


def is_valid(s):
    """Checks whether the input is valid."""
    if s.isdigit() and 1 <= int(s) <= 100:
        return True
    else:
        return False


number, count = randint(1, 100), 0
print('I made a number from 1 to 100. Can you guess it?\n')

while True:
    while True:
        guess_str = input("What's your guess?.. ")
        print()
        if is_valid(guess_str):
            guess = int(guess_str)
            count += 1
            break
        else:
            print('Invalid input. Please enter an integer in the range from 1 to 100.')
    if guess > number:
        print('No, my number is less than yours.')
    elif guess < number:
        print('No, my number is greater than yours.')
    else:
        print(f'Yes, you are correct! It took you {count} attempts to guess my number!')
        break

print('Thanks for playing! Hope to see you again!')
