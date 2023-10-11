# https://www.geeksforgeeks.org/hangman-game-python/

# Imports random library
import random

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
guesses = []

# Notifies the beginning of the game
print("Guess the word! HINT! word is a name of a fruit")

# Checks the game status if won or lost
gameWon = False

# Stores the number of characters of the word
listLength = len(answer)

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
        guess = input("Enter a letter to guess: ")
        if guess in answer:
            answer.count(guess)
        elif guess not in answer:
            print("Wrong!")

except:
    print("The game is ended.")
