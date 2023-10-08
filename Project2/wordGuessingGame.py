# https://www.geeksforgeeks.org/python-program-for-word-guessing-game/

# Random library to be used throughout the game
import random

# Asks the user to input their name
name = input("What is your name? ")

print("Hello {}. Good Luck!".format(name))

# List of the words is added to the game

words = [
    "rainbow",
    "computer",
    "science",
    "programming",
    "python",
    "mathematics",
    "player",
    "condition",
    "reverse",
    "water",
    "board",
    "geeks",
]

# Random answer is chosen at the start of the game
answer = random.choice(words)

# An empty list is used to store the answer word
# Into single characters form
answer_string = []

# Randomly chosen answer is transferred and
# Converted to single characters form
for letter in answer:
    answer_string.append(letter)

# Prints out the answer so that the conversion
# Looks successful
print(answer_string)

# An empty list to store the guesses characters
guess = []

# Number of chance that the player can try
# Also the number of letter of longest word is 11 letters

turns = 12

# Prints out number of chances the player has

print("Guess the characters. You have", turns, "turns remaining")

# Plays it until the player has 0 turns left
while turns > 0:
    # A loop starting from first letter of the answer
    for letter in answer_string:
        # Checks if the guess character matches the answer
        if input("Guess a character: ") == letter:
            # If so, then adds the letter to the guess variable
            guess.append(letter)

            # Prints out the guess variable to display the status
            print(guess)

            # If the number of turns is 0 or greater
            # And guess equals to the answer
            # Print win and break the whole loop
            if turns >= 0 and guess == answer_string:
                print("You won with", turns, "turns left!")
                turns = 0

        # If the number of turns is 0 or less
        # Print lose and break the whole loop
        elif turns <= 0:
            print("You lose!")

        # If the guesses character does not match the answer
        # Print "Not Correct"
        else:
            print("Not correct")

            # Decreases the number of turns left
            turns -= 1
