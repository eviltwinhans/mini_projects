import re


def shift_one_symbol(symbol, shift, flag):
    """Process one given symbol from English or Russian alphabet using the Caesar Cyper algorithm, return a symbol."""
    this_symbol = ord(symbol)
    if 65 <= this_symbol <= 90:  # ord('A') = 65, ord('Z') = 90
        zero_symbol, length = 65, 26
    elif 97 <= this_symbol <= 122:  # ord('a') = 97, ord('z') = 122
        zero_symbol, length = 97, 26
    elif 1040 <= this_symbol <= 1071:  # ord('А') = 1040, ord('Я') = 1071
        zero_symbol, length = 1040, 32
    elif 1072 <= this_symbol <= 1103:  # ord('а') = 1072, ord('я') = 1103
        zero_symbol, length = 1072, 32
    else:
        return symbol
    return chr(zero_symbol + (this_symbol - zero_symbol + flag * shift + length * shift) % length)


def shift_all_symbols(word, shift, flag):
    """Process an English or Russian text using the Caesar Cyper algorithm, return a string."""
    result = ''
    for c in word:
        result += shift_one_symbol(c, shift, flag)
    return result


def divide_et_impera(string):
    """Divide a text into blocks consisting of letters and other characters, return a list."""
    blocks = re.split('(\W+)', string)
    return blocks


encrypt_yes = -1 if input('Enter "D" if you need to decrypt, not encrypt.\n').lower() == 'd' else 1
print('Encryption requested.\n' if (encrypt_yes + 1) else 'Decryption requested.\n')
shift_mode = input('Do you know the shift amount? (Y/N/*)\n').lower()
if shift_mode == 'y':
    shift_amount = int(input('Select shift amount. (0-99)\n'))
    print(f'The procedure will be executed with the right shift of {shift_amount}.\n')
elif shift_mode == 'n':
    print("Let's check different values for the shift amount...")
else:
    print("Special mode enabled! For each word the shift will be equal to its length")
text = input('Enter the text you need to process.\n')

if shift_mode == 'y':
    print(shift_all_symbols(text, shift_amount, encrypt_yes))
elif shift_mode == 'n':
    for i in range(1, 32):
        print(shift_all_symbols(text, i, encrypt_yes))
else:
    temp_list = divide_et_impera(text)
    text_processed = ''
    for item in temp_list:
        text_processed += shift_all_symbols(item, len(item), encrypt_yes)
    print(text_processed)
