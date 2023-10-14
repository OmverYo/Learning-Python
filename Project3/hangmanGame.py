# https://www.geeksforgeeks.org/hangman-game-python/

# Imports random library
import random
from collections import Counter

# Stores list of words to be used throughout the game
words = [
    "apple",
    "banana",
    "mango",
    "strawberry",
    "orange",
    "grape",
    "pineapple",
    "apricot",
    "lemon",
    "coconut",
    "watermelon",
    "cherry",
    "papaya",
    "berry",
    "peach",
    "lychee",
    "muskmelon",
]

# Randomly chooses a word from the list
answer = random.choice(words)

# Stores guesses
guesses = ""

# Notifies the beginning of the game
print("Guess the word! HINT! word is a name of a fruit")

# Checks the game status if won or lost
gameWon = False

# Stores the number of characters of the word
listLength = len(answer)

print(answer)

# Gives the length hint
print("The word is {} letters long.".format(listLength))

# Prints out the length of word using _
for listLength in answer:
    print("_ ", end="")

# Leaves a space between the sentence before it
print("\n")

# Game loop
try:
    while gameWon == False:
        try:
            # Leaves a space between the question and guesses
            print()
            guess = str(input("Enter a letter to guess: "))

        # Prevents an exception typing other than string
        except:
            print("Enter only a string type letter!")
            continue

        # Checks if the guesses letter is in the previously guessed guesses
        if guess in guesses:
            print("You have already guessed that letter")

        # Checks if the guess is correct
        elif guess in answer:
            # Count stores the frequency of guesses appearance
            count = answer.count(guess)

            # Guess is added into guesses
            for _ in range(count):
                guesses += guess

        # Notifies the player that guess is wrong
        elif guess not in answer:
            print("Wrong!")

        # Prints the guessed letters and _ blank spaces for the game
        for char in answer:
            # If the letters from answer are in guesses and
            # the guesses and the answer are not matching
            # print the characters from guesses
            if char in guesses and (Counter(guesses) != Counter(answer)):
                print(char, end=" ")
            # If guesses and the answer are matching
            # print the answer and victory announcement
            elif Counter(guesses) == Counter(answer):
                print("The word is {}.".format(answer), end=" ")
                print("Congratulations, you won!")
                # Sets the while loop condition to True
                gameWon = True
                # and ends the loop to finalise the game
                break

            # Prints _ if the corresponding slot is not guessed yet
            else:
                print("_", end=" ")
except:
    print("The game is ended.")
