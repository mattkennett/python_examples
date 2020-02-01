import random

# The 'as' keyword below isn't strictly necessary, but it helps avoid any namespace collisions.
# To use anything from the file globals.py in this file, I need to prepend the thing I want
# with whatever identifier I use after the 'as' keyword. For example, if I want to use the
# value of NUM_STRIKES_ALLOWED from globals.py in this file, I would use 
# hangman_globals.NUM_STRIKES_ALLOWED because I've chosen 'hangman_globals' as my identifier.
# That way, I could have a variable in this file called NUM_STRIKES_ALLOWED without conflicting
# with the variable from the file globals.py.
import globals as hangman_globals

class Hangman:
    '''
    This is a class for playing a simple game of hangman.

    Attributes:
        strikes_allowed (int): The number of strikes a user gets before losing a game
        puzzle (dict): The puzzle the user is trying to solve. Contains keys 'puzzle' (str) and
            'category' (str)
        guessed_letters (set): The set of letters that a user has already guessed
        unguessed_letters (set): The set of letters that exist in the puzzle but have not been guessed
        strikes (int): The number of strikes the user currently has
    '''

    # Static member variables
    strikes_allowed = hangman_globals.NUM_STRIKES_ALLOWED
    # I'm making this variable static because this value won't change from one instance of class
    # Hangman to another.

    def __init__(self):
        '''
        This function is the constructor for class Hangman.

        The constructor starts a new puzzle by calling the member function start_random_puzzle()
        on the current instance of class Hangman.

        Parameters:
            None
        
        Returns:
            None
        '''

        self.start_random_puzzle()
    
    def start_random_puzzle(self):
        '''
        This function initializes a random puzzle.

        The puzzle is chosen randomly from the list of puzzles defined in globals.py

        Parameters:
            None
        
        Returns:
            None
        '''

        all_puzzles = hangman_globals.PUZZLES
        # Make sure the line below makes sense to you. It might look complicated at first, but
        # it's pretty simple. The first thing that will happen is that random.randint will
        # return a value between 0 and the length of all_puzzles - 1. The variable all_puzzles
        # is a list, so it can be accesed by index. This line says "give me a random but valid
        # element from all_puzzles and set that element as self.puzzle."
        self.puzzle = all_puzzles[random.randint(0, len(all_puzzles) - 1)]
        self.guessed_letters = set()

        # I'm converting all of the letters in the puzzle to uppercase before placing
        # them in the unguessed_letters set to make comparison simpler.
        self.unguessed_letters = set(char for char in self.puzzle['puzzle'].upper())
        # The line above is just saying "iterate through each character in my puzzle and add
        # the uppercase representation of that character to the set. Then save that set as 
        # self.unguessed_letters."
        self.strikes = 0
    
    def get_game_state(self):
        '''
        This function returns the current state of a game.

        If the user is out of strikes, they lose. If the user has guessed all of the
        letters, they win. Otherwise, the game is still in progress.

        Parameters:
            None
        
        Returns:
            None
        '''

        if self.strikes == self.strikes_allowed:
            return 'lose'
        elif not self.unguessed_letters:
            return 'win'
        else:
            return 'in_progress'

    def update_game(self, guess):
        '''
        This function updates the state of a game.

        A user's guess is passed to this function. The incoming guess is converted
        to upper case and any characters after the first are ignored. An asterisk
        means that the player has given up. 

        If an asterisk is passed to the function, the game is set to the losing
        state. If an alphabetic character is passed to the function, the game state
        is updated with that character. Otherwise, the game state is not changed.

        Parameters:
            guess (str): The user's guess
        '''
        safe_guess = guess[:1].upper()
        if safe_guess == '*':
            self.strikes = self.strikes_allowed
            return 
        
        if not safe_guess.isalpha() or safe_guess.upper() in self.guessed_letters:
            # If the user's input isn't an alphabetic character or it has already 
            # been guessed, we're just going to ignore it.
            # "I don't understand the question, and I won't respond to it."
            #   --Lucille Bluth
            return

        if safe_guess.upper() in self.unguessed_letters:
            # If the guess is in the set of unguessed letters, that letter is
            # no longer unguessed. 
            self.unguessed_letters.remove(safe_guess.upper())
        else:
            # Otherwise, the user gets a strike.
            self.strikes += 1
        
        # The letter should be added to the set of guessed_letters either way.
        self.guessed_letters.add(safe_guess.upper())
        

# The line below tells Python where the entry point should be when the file hangman.py is
# invoked by the Python interpreter. This is just a utility file, so there's no need to
# ever invoke this file. We'll just let the user know that.
if __name__ == '__main__':
    print('Please launch main.py rather than hangman.py')
