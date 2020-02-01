import random
# We need the random library to select a random puzzle

def make_puzzle_string(puzzle, unguessed_letters):
    '''
    This function returns the obfuscated puzzle as a string.

    Obfuscated puzzle means the puzzle string with any unguessed letters replaced by blanks.
    For readability, each character will be given one whitespace padding. Blanks will be 
    represented with underscores.

    Parameters:
    puzzle (dict): a dictionary with keys for 'puzzle' and 'category'
    unguessed_letters (set): a set containing puzzle letters that haven't been guessed yet

    Returns:
    (string): representation of the puzzle
    '''
    puzzle_string = ''
    for char in puzzle['puzzle']:
        if char.upper() in unguessed_letters:
            puzzle_string += ' _ '
        else:
            puzzle_string += ' %s ' % char
    return puzzle_string

# This is a list of dictionaries
puzzles = [
    {'category': 'Programming Languages', 'puzzle': 'Python'},
    {'category': 'Programming Languages', 'puzzle': 'JavaScript'}
]

strikes_allowed = 3
strikes = 0

# random.randint(first, last) will return a random integer between first and last inclusive.
# Using the values 0 and len(puzzles) - 1, the integer returned will be a random *but valid*
# index for the list
roll = random.randint(0, len(puzzles) - 1)
puzzle = puzzles[roll]

# A Python set is an *unordered* collection of hashable types. A "hashable type" is one that
# can trivially be run through a hashing algorithm like a string or integer. More complex
# types aren't hashable and if you're not sure if a type is hashable, Python is kind enough
# to let you know if you ever try to hash something that's unhashable.
unguessed_letters = set()

# Python strings quack like lists of characters, so Python's duck typing will treat a string
# as an iterable collection of characters. That's why my for loop is simply 
# 'for char in puzzle['puzzle'] (Remember that the variable puzzle is a dictionary that 
# has a key called puzzle.) The call to .upper() at the end of the line will transform the
# puzzle['puzzle'] into all uppercase characters (if necessary [calling upper() on a string 
# (or substring) that is already uppercase won't hurt anything]). That will make comparison
# easier later.
for char in puzzle['puzzle'].upper():
    # You'll never believe this, but the add() method is used to add items to a set. It's
    # safe to call add() on an item that already exists in the set, but sets don't have any
    # sort of counter for how many times an item has been added. A set will be exactly the
    # same if you add the same element once or a million times.
    unguessed_letters.add(char)

print('Welcome to Python Hangman!')
print('Your category is: %s' % puzzle['category'])


while unguessed_letters and strikes < strikes_allowed:
    # The funky line below does the following:
    # We're putting a string together and it has two variables. The first is an integer
    # and the second is a string. The integer's value is calculated by subtracting
    # strikes from strikes_allowed. The string will evaluate to 's' if there's more than
    # one strike left and will evalute to '' (an empty string) otherwise.
    print('You have %d strike%s remaining.' % (strikes_allowed - strikes, 's' if (strikes_allowed - strikes) > 1 else ''))
    print(make_puzzle_string(puzzle, unguessed_letters))
    # The call to upper() below will transform the character from our user to uppercase
    guess = input('Guess:').upper()

    # Another fantastic thing about Python strings is that dealing with substrings is 
    # incredibly easy. In the line below, guess[:1] is telling Python to start at the
    # beginning of the string and read exactly one character. We'll talk a lot more about
    # string manipulation in class.

    # So, in the if statement below, guess[:1] is giving us the first character of our
    # dear user's input (and we've already converted it to uppercase. We also converted
    # all of the letters in unguessed_letters to uppercase before we put them in the set.
    # Remember what I said about "making comparison easier" up above?)
    # Since Python strings quack like iterables of characters, we can use the 'in' keyword
    # to see if a character exists in a string. The expressivity of this language is just
    # wonderful, don't you think?
    if guess[:1] in unguessed_letters:
        # The remove() method will remove an item from a set. However, unlike the add()
        # method, it's not safe to call remove() on an item that doesn't exist in a set.
        # If you try to do that, Python will throw a KeyError right at your face. So, it's
        # always a good practice to check to be sure that a key exists in a set before
        # trying to remove it because it's not pleasant when Python throws things at your face.
        unguessed_letters.remove(guess[:1])
    else:
        # If the user's guess isn't in the set of unguessed letters, this version of the game
        # is going to call that a strike. That means that a user will get a strike if they
        # guess a character a second time, even if it's actually in the puzzle. This version
        # of the game is pretty brutal.
        strikes += 1

if strikes < strikes_allowed:
    print('You win! :)')
else:
    print('You lose. :(')

print('The word was: %s' % puzzle['puzzle'])
