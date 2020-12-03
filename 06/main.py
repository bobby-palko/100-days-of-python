import random
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False

# We give 6 lives to match the 'stages' of ASCII art
lives = 6

# Randomly choose one work to play
chosen_word = random.choice(word_list)

# I did promise some sweet ASCII art 
print(logo)

# Build out answer display
display = []
for _ in chosen_word:
    display.append("_")

# Keep track of player guesses
guesses = []


while not end_of_game:

    # Take the user's guess and make it lowercase to compare against the chosen_word
    guess = input("Guess a letter: ").lower()

    # Let the player know if they've already guessed that letter. Don't penalize them for double guesses
    if guess in guesses:
        print(f"You've already guessed '{guess}'. Pick a different letter")
        continue
    else:
        guesses.append(guess)
    

    # Check if the letter matches anywhere in the chosen_word and update display to show it
    for i in range(len(chosen_word)):
        # Fill in all the blanks where the guessed letter  exists
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]

    # Once we've checked, if the guess isn't in the word lose a life
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess.upper()} is not in the word. You lose a life.")

    # Combine all the elements of the list into a String for UI
    print(f"{' '.join(display)}")

    # Show that sweet ASCII art corresponding to how many lives are left
    print(stages[lives])

    # Check if any more blanks are left. If not, the player has won
    if "_" not in display:
        end_of_game = True
        print("You won!")
    elif lives == 0:
        end_of_game = True
        print(f"You lose. The word was {chosen_word}.")

