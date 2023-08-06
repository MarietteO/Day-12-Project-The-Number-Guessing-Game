import random
from art import logo

def generate_random_number():
    """Generates a random number between 1 and 100."""
    num = random.randint(1, 100)
    return num


def difficulty(chosen_level):
    """Maps the selected difficulty level to the number of allowed turns."""
    if chosen_level == "easy":
        return 10
    elif chosen_level == "hard":
        return 5
    else:
        return False


def guess(answer):
    """Handles the guessing process by prompting the user to guess the number."""
    while True:
        user_num = int(input("Please guess the number: "))
        if user_num > answer:
            print("Too high")
            return True
        elif user_num < answer:
            print("Too low")
            return True
        else:
            print("That's it! You win!")
            return False

print(logo)
print("Welcome to the Number Guessing Game!")

loop = True
while loop:
    rand_num = generate_random_number()
    level = input("I'm thinking of a number between 1 and 100. Please choose a level. Type 'easy' or 'hard': ").lower()
    print(f"Psst, the number is {rand_num}.")
    difficulty_level = difficulty(level)
    if not difficulty_level:
        print("That answer is not valid.")
    elif difficulty_level:
        turns = difficulty_level
        for _ in range(difficulty_level):
            user_guess = guess(rand_num)  # Get the result of the user's guess
            turns -= 1
            if not user_guess:  # If the user guessed correctly
                break
            elif turns == 0:
                print(f"Your turns are up! The answer was {rand_num}.")
                break
        play_again = input("Would you like to play again? Type 'y' for yes or any other key for no: ").lower()
        if play_again == "y":
            pass
        else:
            loop = False
