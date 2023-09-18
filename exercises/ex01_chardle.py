"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730663941"


word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

else: 
    character: str = input("Enter a single character: ")
    
    if len(character) != 1:
        print("Error: Character must be a single character.")
        exit()
    else: 
        char_count: int = 0
        print("Searching for " + character + " in " + word)

        if word[0] == character:
            print(character + " found at index 0")
            char_count += 1
        if word[1] == character:
            print(character + " found at index 1")
            char_count += 1
        if word[2] == character: 
            print(character + " found at index 2")
            char_count += 1
        if word[3] == character:
            print(character + " found at index 3")
            char_count += 1
        if word[4] == character:
            print(character + " found at index 4")
            char_count += 1

        if char_count == 0: 
            print("No instances of " + character + " found in " + word)

        elif char_count == 1:
            print("1 instance of " + character + " found in " + word)

        else:
            print(str(char_count) + " instances of " + character + " found in " + word)