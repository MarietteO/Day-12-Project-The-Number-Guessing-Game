# A shorter solution

import random

TURNS = 0

secret_number = random.randint(0, 100)

print("Welcome to the Number Guessing Game!")
choose_mode = (input("I'm thinking of a number between 1 and 100. Please choose a level. Type 'easy' or 'hard': ")
               .lower())
if choose_mode == "hard":
    TURNS = 5
else:
    TURNS = 10
for _ in range(TURNS):
    guess = int(input("Please guess the number: "))
    if guess > secret_number:
        print("That is too high.")
    elif guess < secret_number:
        print("That is too low")
    else:
        print("That's it!")
print(f"Turns are up! The secret number was {secret_number}.")
