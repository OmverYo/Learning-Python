#https://www.geeksforgeeks.org/number-guessing-game-in-python/

import math
import random

lower = int(input("Enter your lower bound: "))

upper = int(input("Enter your upper bound: "))

answer = random.randint(lower, upper)

guesses = round(math.log(upper - lower + 1, 2))

print("You have only", guesses, "guesses!")

count = 0

while count < guesses:
    count += 1

    guess = int(input("Guess a number: "))

    if guess == answer:
        print("You are right!")
        break

    elif guess < answer:
        print("You guessed it too small")
    
    elif guess > answer:
        print("You guesses it too high")

if count >= guesses:
    print("The answer is", answer)