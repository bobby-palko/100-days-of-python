# CPU picks a number between 1 and 100
# Two modes: easy and hard
#  - easy gets 10 guesses, hard gets 5
# Let the player know if they're too high or too low

import random
from art import logo
from os import name, system

def clearScreen():
    # for windows
    if name == "nt":
        system("cls")
    #linux and macOS
    else:
        system("clear")

def check_guess():
    if guessed_number > number_to_guess:
        return "Too high."
    else:
        return "Too low."

# Sweet ASCII art
print(logo)

# To allow the user to play again without restarting
is_playing = True

while is_playing:
    # Greeting
    print("Welcome to the Number Guessing Game!")

    # Generate number for player to try and guess
    number_to_guess = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100.")

    # Set the difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        guesses = 10
    else:
        guesses = 5

    # Let the user keep guessing as long as they have lives
    while guesses > 0:
        print(f"DEBUG: number = {number_to_guess}; guesses = {guesses} ")
        print(f"You have {guesses} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))
        if guessed_number == number_to_guess:
            guesses = -1
            print("You guessed the number. You win!")
        else:
            guesses -= 1
            print(check_guess())
            if guesses > 0:
                print("Guess again.")
    if guesses == 0:
        print("You lose.")

    continue_playing = input("Would you like to play again? Y/N: ").lower()
    if continue_playing == 'y':
        is_playing = True
        clearScreen()
    else:
        is_playing = False