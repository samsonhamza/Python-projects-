# Here is a guess the number game.

import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I am thinking of a number between 1 and 100.")
    print("You have to guess the number. Let's see how many tries it takes!\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()