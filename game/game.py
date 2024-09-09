import random

# initialize while loop.
while True:
    # ask user for the stop value of the range.
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
    except ValueError:
        # handle non-numeric input
        print("Please enter valid positive integer.")


# store random value in a variable        
random_int = random.randint(1, level)

# initialize while loop for the game. 
while True:
    user_input = int(input("Guess: "))
    # if, elif, and else for the 3 possible conditions of the games.
    try:
        if random_int > user_input:
            print("Too small!")
        elif random_int < user_input:
            print("Too large!")
        else:
            print("Just Right!")
            break
    except ValueError:
        # handle non-numeric input
        print("Please enter a valid integer.")

print("End of Game!")