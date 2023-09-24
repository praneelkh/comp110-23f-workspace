""" EX03 - WORDLE. """

__author__ = "730663941"

# Defining the "contains_char" function for "emojified" function
def contains_char(searched_string: str, single_char: str) -> bool:
    """Checks for a single character in a given string"""

    # Error if 2nd argument is not valid
    assert len(single_char) == 1

    word_index: int = 0
    # Iterating through a string to see if the character matches anywhere
    while word_index < len(searched_string):
        if searched_string[word_index] == single_char:
            return True
        else:
            word_index += 1
    return False

# Defining the "emojified" function to print a string of emoji boxes        
def emojified(guess_word: str, secret_word: str) -> str:
    """Checks for any matching characters between two strings and returns a string of corresponding emoji boxes"""
    
    # Error if lengths of the arguments are different
    assert len(guess_word) == len(secret_word)
    
    # Assigning emoji codes to variables
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    # Initilizing an index for the guess and an empty emoji box string
    guess_idx: int = 0
    emoji_boxes: str = ""

    while guess_idx < len(secret_word):
        # If correct letter is in correct place
        if guess_word[guess_idx] == secret_word[guess_idx]:
            emoji_boxes += GREEN_BOX
        # If correct letter is in wrong place
        elif contains_char(secret_word, guess_word[guess_idx]) is True:
            emoji_boxes += YELLOW_BOX
        # If wrong letter
        else:
            emoji_boxes += WHITE_BOX
        guess_idx += 1
    return emoji_boxes

# Defining "input_guess" function to obtain a valid input from the user
def input_guess(expected_length: int) -> str:
    """Obtains a valid input from user"""
    # Initializing guess to user input
    guess: str = input(f"Enter a {expected_length}-character word: ")
    # Keep prompting user until a valid input is given
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    
    secret: str = "codes"
    turn_number: int = 1
    
    # Gives player 6 chances
    while turn_number < 7:
        print(f"=== Turn {turn_number}/6 ===")
        user_guess: str = input_guess(len(secret))
        # Prints emoji box string based on the input
        print(emojified(user_guess, secret))
        if user_guess == secret:
            # Winning Message
            print(f"You won in {turn_number}/6 turns!")
            return None
        else:
            turn_number += 1
    # Losing Message
    print("X/6 - Sorry, try again tomorrow!")
    return None

if __name__ == "__main__":
    main()