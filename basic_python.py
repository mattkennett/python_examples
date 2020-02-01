import random

def categorize_guess(guess, answer, valid_min, valid_max):
    if guess == answer:
        return 'Correct'
    if guess != answer and guess >= valid_min and guess <=valid_max:
        return 'Reasonable, but incorrect'
    else:
        return 'Pants on head stupid'

# This is a single line comment
'''
This is a multi-
line comment
'''
roll = random.randint(1, 6)
print(roll)
guess = 0
guess_count = 0

while roll != guess:
    guess = int(input('Make a guess between 1 and 6: '))
    print('Your Guess Was: %s' % categorize_guess(guess, roll, 1, 6))

    guess_count += 1

print('It took you %d attempt%s to '\
    'guess correctly.' % (guess_count, 's' if guess_count > 1 else ''))

