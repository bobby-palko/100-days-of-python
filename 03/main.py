# This is our "AI"
import random

# Some more sweet ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Make a list of the available choices in the game
game_options = [rock, paper, scissors]

# Welcome!
print("Let's play Rock, Paper, Scissors!")

# Make a choice
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))

# Computer chooses randomly
cpu_choice = random.randint(0,2)

# Someone didn't follow the rules
if player_choice > 2 or player_choice < 0:
    print("Invalid number, you lose!")
else:
    # Now we can safely assign art and display it
    player_art = game_options[player_choice]
    cpu_art = game_options[cpu_choice]

    print(player_art)
    print(f"Computer chose:\n{cpu_art}")

    # Determine the winner
    # Check for a rock/scissots matchup
    if player_choice == 0 and cpu_choice == 2:
        # player rock beats cpu scissors
        print("You win!")
    elif cpu_choice == 0 and player_choice == 2:
        # cpu rock beats player scissors
        print("You lose.")
    # each item in the list beats the one immediately below it
    elif player_choice > cpu_choice:
        print("You win!")
    elif cpu_choice > player_choice:
        print("You lose.")
    # eh, we'll call it a draw
    else:
        print("Draw.")