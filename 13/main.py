
# logo should stay "fixed" at top of screen

# HIGHER LOWER
# Current score (not displayed on first round)
# Compare A: Person, a Role, from Place
# VS ART
# Against B: Person, a Role, from Place
# Who has more followers? Type 'A' or 'B': 

# if they guess right, increase score,
#  'A' = 'B', get new 'B'
# 'A' and 'B' should be a list
from game_data import data
import random
from art import logo, vs
from os import name, system

# finally made this snake_case
def clear_screen():
    # for windows
    if name == "nt":
        system("cls")
    #linux and macOS
    else:
        system("clear")

def no_twins(person):
    """
    Makes sure we do not compare someone against themselves
    """
    new_person = random.choice(data)
    # Keep swapping out the new_person until it's someone different
    while new_person.get('follower_count') == person.get('follower_count'):
        new_person = random.choice(data)
    
    return new_person

def determine_winner(a, b):
    if a > b:
        return "a"
    else:
        return "b"

def goes_to_next_round(guess, answer):
    if guess == answer:
        increase_score()
        return True
    else:
        return False

def increase_score():
    global score
    score += 1

still_winning = True

 # load person B on init for swap to work in while loop
person_b = random.choice(data)

score = 0

while still_winning:

    person_a = person_b
    
    # make sure the second person isn't the same as the first
    person_b = no_twins(person_a)

    clear_screen()

    print(logo)

    if score != 0:
        print(f"That's right! Current score: {score}")

    # display our battle
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")
    
    answer = determine_winner(person_a['follower_count'], person_b['follower_count'])
    
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    still_winning = goes_to_next_round(choice, answer)

print(logo)
print(f"Sorry, that's wrong. Final score: {score}.")