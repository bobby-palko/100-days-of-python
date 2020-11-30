# Some cool ASCII art from ascii.co.uk 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island! Your missing is to find the treasure")

choice = input("You start at a crossroads. Do you go left or right? ").lower()

# is it better to swap the if/else checks so it's not a 'NOT' comparator? :shrug:
if choice != "left":
    print("You have fallen into a hole. Game Over.")
else:
    choice = input("You approach a shore with an island in the distance. Do you swim or wait? ").lower()
    if choice != "wait":
        print("Shark bait ooh-ha-ha! Game Over.")
    else:
        choice = input("You see three doors: red, blue, or yellow. Which do you pick?").lower()
        if choice == "yellow":
            print("You found the gold! You win!")
        elif choice == "red":
            print("Is it hot in here or is it just me? Consumed by fire. Game Over.")
        elif choice == "blue":
            print("Well, you found where the fantastic beasts are. And they're hungry. Game Over.")
        else:
            print("Thinking there's another color, you smash into the wall. Game Over.")