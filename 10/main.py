import random
from os import name, system
from art import logo

def clearScreen():
    # for windows
    if name == "nt":
        system("cls")
    #linux and macOS
    else:
        system("clear")

def deal_card(hand):
    """
    Appends a random value from the cards list to the hand passed in.
    """
    hand.append(random.choice(cards))

def calculate_score(hand):
    """
    Returns the blackjack score of the hand passed in.
    If it's determined the hand has blackjack, returns 0.
    """

    # Check for blackhack first
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    # If we're over 21, check for an Ace and give it the lower value
    elif sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    
    return sum(hand)

# Our "deck of cards"
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_playing = True

while is_playing:

    new_game = input("Do you want to play a game of Blackjack? Y/N: ").lower()
    
    if new_game == 'y':

        # Do the needfuls and clear out old data
        clearScreen()
        player_hand = []
        cpu_hand = []

        print(logo)

        # Deal the starting hands
        deal_card(player_hand)
        deal_card(cpu_hand)
        deal_card(player_hand)
        deal_card(cpu_hand)

        player_score = calculate_score(player_hand)
        cpu_score = calculate_score(cpu_hand)

        print(f"\tYour cards: {player_hand}, current score: {player_score}")
        print(f"\tComputer's first card: {cpu_hand[0]}")

        # Check for blackjack and continue playing if neither has it
        if player_score > 0 and cpu_score > 0:
            dealing_to_player = True
            while dealing_to_player:
                next_card = input("Type 'y' for another card, or 'n' to pass: ").lower()
                if next_card == 'y':
                    deal_card(player_hand)
                    player_score = calculate_score(player_hand)
                    if player_score >= 21:
                        dealing_to_player = False
                    print(f"\tYour cards: {player_hand}, current score: {player_score}")
                    print(f"\tComputer's first card: {cpu_hand[0]}")
                else:
                    dealing_to_player = False
            # CPU always takes a card when they're under 17
            while cpu_score < 17:
                deal_card(cpu_hand)
                cpu_score = calculate_score(cpu_hand)
        
        # Done dealing, show the final results
        print(f"\tYour final hand: {player_hand}, final score: {player_score}")
        print(f"\tComputer's final hand: {cpu_hand}, final score: {cpu_score}")

        # Determine who won
        if player_score > 21:
            print("You went over. You lose")
        elif player_score == cpu_score:
            print("Draw")
        elif player_hand == 0:
            print("You win with blackjack!")
        elif cpu_score == 0:
            print("Computer got blackjack. You lose.")
        elif player_score > cpu_score:
            print("You win!")
        elif cpu_score > 21:
            print("Opponent went over. You win!")
        elif cpu_score > player_score:
            print("You lose.")
        else:
            print("What condition did I miss?")
    else:
        is_playing = False
