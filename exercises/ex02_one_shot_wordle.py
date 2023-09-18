"""EX02 - One Shot Wordle."""

__author__ = "730663941"

# Initializing secret word, guess, and guess index
secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
guess_idx: int = 0

# Easy access codes for emoji boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Blank string for emoji boxes output 
emoji_boxes: str = ""

# Obtaining a VALID input
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

# If guess does not match secret word
if guess != secret_word:
    while guess_idx < len(secret_word):
        # Adding green box for correct letter in the correct place

        if guess[guess_idx] == secret_word[guess_idx]:
            emoji_boxes += GREEN_BOX

        else: 
            # Comparing a single letter from the guess to every letter in secret word
            matching_char: bool = False
            alt_idx: int = 0 
            while matching_char == False and alt_idx < len(secret_word):
                if guess[guess_idx] == secret_word[alt_idx]:
                    matching_char = True
                else:
                    alt_idx += 1
            # Adding yellow box if correct letter is in wrong place
            if matching_char == True:
                emoji_boxes += YELLOW_BOX
            # Adding a white box if wrong letter
            else:
                emoji_boxes += WHITE_BOX
        guess_idx += 1
    # Output Messages
    print(emoji_boxes)
    print("Not quite. Play again soon!")

# If the guess matches the secret word
elif guess == secret_word:
    while guess_idx < len(secret_word):
        emoji_boxes += GREEN_BOX
        guess_idx += 1
    print(emoji_boxes)
    print("Woo! You got it!")

    
