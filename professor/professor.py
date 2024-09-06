import random

def main():
    # Call get_level
    level = get_level()
    # Get the score
    score = simulate_game(level)
    # Print the score
    print("Score: ", score)


def get_level():
    # Get the level from the user.
    while True:
        try:
            level = int(input("Enter Level 1, 2, or 3: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    # Depending on the level, generate random integers.
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


# Simulate a single round of math problems
def simulate_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False


# Simulate the full game
def simulate_game(level):
    count_rounds = 1
    score = 0
    while count_rounds <= 10:
        x, y = generate_integer(level)
        response = simulate_round(x, y)
        if response:
            score += 1
        count_rounds += 1
    return score


if __name__ == "__main__":
    main()