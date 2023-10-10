# https://www.geeksforgeeks.org/hangman-game-python/

import random

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

answer = random.choice(words)

answer_string = []

for letter in answer:
    answer_string.append(letter)

print(answer_string)
print(len(answer_string))

print("Guess the word! HINT! word is a name of a fruit")

gameWon = False
listLength = len(answer_string)

for listLength in answer_string:
    print("_ ", end="")

while gameWon == False:
    input("Enter a letter to guess: ")
