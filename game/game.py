# In a file called game.py, implement a program that:
# - Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
# - Randomly generates an integer between 1 and n, inclusive, using the random module.
# - Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# # - If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# # - If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# # - If the guess is the same as that integer, the program should output Just right! and exit.

import random
import sys

def main():
    level = get_integer("Level: ")

    number = random.randint(1, level) # Random integer between 1 and n

    while True:
        guess = get_integer("Guess: ")
        if guess < number:
            print("Too small!")
            continue
        elif guess > number:
            print("Too large!")
            continue
        else:
            print("Just right!")
            sys.exit() # 'break' and 'return' weren't working as intended, check50 reported a timeout while 'python game.py' ran smoothly. Resorted to system exit

# Function that handles positive integer input
def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            continue

main()
