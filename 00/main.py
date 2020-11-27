# Program greeting
print("Welcome to the Band Name Generator!")

# Ask the user for the name of a pet
pet_name = input("What is your pet's name?\n")

# Ask the user for an adjective
adjective = input("Give me an adjective:\n")

# Ask for a plural noun
plural_noun = input("How about a plural noun?\n")

# Combine the inputs to show their band name
# The capitalize() function is out of the scope of day 1 (I think it comes later), but I wanted to make the strings look better.
print('Your band name is "' + pet_name.capitalize() + ' and the ' + adjective.capitalize() + ' ' + plural_noun.capitalize() + '."')