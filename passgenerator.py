import random as rnd


def generate_password(pass_length, pass_symbols):
    """Generate and return a string of specified valid symbols and of specified length."""
    n, password = len(pass_symbols), ''
    for _ in range(pass_length):
        password += pass_symbols[rnd.randrange(n)]
    return password


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
AMBIGUOUS = '1iIlL0oO'
chars = ''

amount = int(input('How many passwords do you need? (1-10)\n'))
length = int(input('What should be the length of each password? (4-99)\n'))
digits_yes = False if input('Should passwords contain digits? (Y/N)\n').lower() in ['n', 'no'] else True
uppercase_yes = False if input('Should passwords contain capital letters? (Y/N)\n').lower() in ['n', 'no'] else True
lowercase_yes = False if input('Should passwords contain lowercase letters? (Y/N)\n').lower() in ['n', 'no'] else True
special_yes = False if input('Should passwords contain special symbols? (Y/N)\n').lower() in ['n', 'no'] else True
ambiguous_yes = True if input('Should passwords contain ambiguous symbols? (Y/N)\n').lower() in ['y', 'yes'] else False

if digits_yes:
    chars += DIGITS
if uppercase_yes:
    chars += UPPERCASE_LETTERS
if lowercase_yes:
    chars += LOWERCASE_LETTERS
if special_yes:
    chars += PUNCTUATION
if not ambiguous_yes:
    for c in AMBIGUOUS:
        chars.replace(c, '')

if chars == '':
    print('The set of valid symbols is empty. Passwords cannot be generated.\n')
else:
    for _ in range(amount):
        print(generate_password(length, chars))