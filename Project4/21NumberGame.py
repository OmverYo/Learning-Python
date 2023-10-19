# https://www.geeksforgeeks.org/21-number-game-in-python/

import time

def lose():
    print("You lose!")
    time.sleep(2)
    exit(0)

def start():
    print("Starting game")

    while True:
        try:
            print("Enter '1' to play first or '2' to play second")

            play = input("> ")

            if play == "1":
                print("Playing first")

            elif play == "2":
                print("Playing second")
                
        except:
            print("Error occured!")
            break

gameProcess = True

print("Welcome to 21 Number Game!")

while gameProcess == True:
    try:
        answer = str(input("Do you want to play the game? (Y / N)"))
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

            else:
                print("Only Y or N are allowed!")
        
        else:
            print("Only Y or N are allowed!")

    except:
        print("Ending the game")
        break