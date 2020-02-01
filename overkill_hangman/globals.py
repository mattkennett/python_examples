# Making a new file to hold two global constants is absurd overkill for
# this tiny little program. I'm just doing this as an example of how to
# define a globals module that can be included in other .py files
# In the real world, I'd probably just put these two variables in the file
# hangman.py. Using all capital letters for constant values is a fairly
# standard programming convention. However, in Python, these values are not
# actually constant because they could be updated. It is standard practice
# to treat variables that are all uppercase as if they are constant.
NUM_STRIKES_ALLOWED = 3

PUZZLES = [
    {'category': 'Programming Languages', 'puzzle': 'Python'},
    {'category': 'Programming Languages', 'puzzle': 'JavaScript'}
]


# The line below tells Python where the entry point should be when the file globals.py is
# invoked by the Python interpreter. This is just a utility file, so there's no need to
# ever invoke this file. We'll just let the user know that.
if __name__ == '__main__':
    print('Please launch main.py rather than globals.py')
