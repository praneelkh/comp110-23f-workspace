"""EX02 - One Shot Wordle."""

__author__ = "730663941"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
guess_idx: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

emoji_boxes: str = ""

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

if guess != secret_word:
    while guess_idx < len(secret_word):
        if guess[guess_idx] == secret_word[guess_idx]:
            emoji_boxes += GREEN_BOX

        else: 
            matching_char: bool = False
            alt_idx: int = 0 
            while matching_char == False and alt_idx < len(secret_word):
                if guess[guess_idx] == secret_word[alt_idx]:
                    matching_char = True
                else:
                    alt_idx += 1
            if matching_char == True:
                emoji_boxes += YELLOW_BOX
            else:
                emoji_boxes += WHITE_BOX
        guess_idx += 1
    print(emoji_boxes)
    print("Not quite. Play again soon!")


elif guess == secret_word:
    while guess_idx < len(secret_word):
        emoji_boxes += GREEN_BOX
        guess_idx += 1
    print(emoji_boxes)
    print("Woo! You got it!")

    
