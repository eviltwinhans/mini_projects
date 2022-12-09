import random


def choice(options):
    """Randomly choose one element from the list specified as a parameter"""
    n = len(options)
    i = random.randrange(n)
    return options[i]


answers = ['Very doubtful', 'Outlook not so good', 'My sources say no', 'My reply is no', 'Don’t count on it',
           'Concentrate and ask again', 'Cannot predict now', 'Better not tell you now', 'Ask again later',
           'Reply hazy, try again', 'Yes', 'Signs point to yes', 'Outlook good', 'Most likely', 'As I see it, yes',
           'You may rely on it', 'Yes — definitely', 'Without a doubt', 'It is decidedly so', 'It is certain']
flag = True
print("Hello there, I'm the Magic 8 Ball and I can answer any question you have!\n")
username = input("What's your name?\n")
print(f"Hi, {username}! Glad to meet you!\n")

while flag:
    question = input("You may enter your question...\n")
    random.seed(len(question))
    print(choice(answers) + '\n')
    while True:
        repeater = input("Do you want to ask again? (Y/N)\n")
        if repeater.lower() in ['y', 'yes']:
            break
        elif repeater.lower() in ['n', 'no']:
            print(f'Okay {username}, hope I did help you a bit. Please come back anytime!')
            flag = False     # finishes the main cycle
            break
        else:
            print('So, is it a "yes" or a "no"?')
