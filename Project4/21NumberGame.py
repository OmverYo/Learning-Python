# https://www.geeksforgeeks.org/21-number-game-in-python/

import time

def lose():
    print("You lose!")
    exit(0)

def start():
    print("Starting game")

gameProcess = True

while gameProcess == True:
    print("Welcome to 21 Number Game!")
    try:
        answer = str(input("Do you want to play the game? (Y / N)"))
    
    except:
        print("Only Y or N are allowed!")
        continue

    if answer == "Y":
        start()
    
    elif answer == "N":
        try:
            quit = str(input("Quit the game? (Y / N)"))
        
        except:
            print("Only Y or N are allowed!")
            continue

        if quit == ("Y"):
            print("You are quitting the game...")
            time.sleep(2)
            exit(0)

        elif quit == ("N"):
            print("Continuing to play...")