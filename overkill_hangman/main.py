from hangman import Hangman


def print_game_state(game):
    '''
    This function prints the status of an instance of class Hangman to the console.

    This function has been implemented outside of class Hangman to separate the concerns of logic
    and presentation. Class Hangman takes care of the logic of the game and the presentation happens
    here. Don't worry too much if the concept of separation of concerns isn't crystal clear right
    now. We're going to talk about it so much this semester that you'll probably get sick of it.

    Parameters:
    None

    Returns:
    None
    '''

    if game.get_game_state() == 'win':
            print('You Win!')
    elif game.get_game_state() == 'lose':
        print('You lose...')
    else:
        # The line below is explained in the other hangman example
        print('You have %d strike%s remaining.' % (game.strikes_allowed - game.strikes, 's' if (game.strikes_allowed - game.strikes) > 1 else ''))
        puzzle_string = ''

        # For each character in the puzzle, this loop will either display the character or
        # ' _ ' depending on whether or not the user has guessed the letter
        for char in game.puzzle['puzzle']:
            puzzle_string += ' _ ' if char.upper() in game.unguessed_letters else ' %s ' % char
        print(puzzle_string)


def game_loop():
    # The line below shows the syntax for creating an instance of a class. We need the
    # parentheses after Hangman() here even though we're not passing in any parameters
    # because we need to tell Python that we want an *instance* of the class and not
    # the *class itself*.
    my_game = Hangman()
    print('#-=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=-#')
    print('Welcome to Python Hangman!')
    print('#-=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=-#')
    print('Your category is: %s' % my_game.puzzle['category'])

    # game_on determines whether or not we will play another game. It's initialized to 'Y'
    # because that's the value that means "play another game" and I'm assuming that my user
    # wants to play a game. You know, since they ran the program and everything. :)
    game_on = 'Y'

    while game_on.upper() == 'Y':
        while my_game.get_game_state() == 'in_progress':
            # As long as the game is in progress, we need to print out the game's state,
            # get a guess from our user, and then update the game wtih that state.
            print_game_state(my_game)
            guess = input('Guess (* to give up):')
            my_game.update_game(guess)
        # Game state needs to be presented to the user once more after the game completes
        # so that they can see the results of their game. It would be rude to keep it a
        # secret from them.
        print_game_state(my_game)
        print('#-=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=-#')

        # A new game is prepared in case our user wants to play again.
        my_game.start_random_puzzle()

        game_on = input('Play again? (y/n):')
        while game_on.upper() not in ['Y', 'N']:
            game_on = input(
                'Input y or n. I\'m trying to be a cool program here and will let you input Y or N even though I didn\'t tell you those would work. But those are the options. YOU WILL CHOOSE ONE OF THEM. DON\'T YOU DARE PRESS CTRL+C TO QUIT THIS PROGRAM. I AM THE ONE WHO KNOCKS!')

    # It never hurts to be polite.
    print('Thanks for playing!')


# The line below tells Python where the entry point should be when the file main.py is
# invoked by the Python interpreter. You can think if this function like the main()
# function in a C/C++ program.
if __name__ == '__main__':
    game_loop()
