MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

def print_report():
    """Prints the current amount of resources in the machine"""

    print(f"""
    Water: {resources['water']}ml
    Milk: {round(resources['milk'], 2)}ml
    Coffee: {resources['coffee']}g
    Money: ${resources['money']}
    """)

def has_resources(drink_name):
    """
    Checks the amount of resources available against what is needed to make the drink.
    Returns a boolean stating whether we have enough resources. 
    """

    drink_ingredients = MENU[drink_name]['ingredients']

    for ingredient in drink_ingredients:
        if resources[ingredient] < drink_ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def collect_coins():
    """Prompts the user for payment and returns the total of the coins deposited"""

    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01

    return quarters + dimes + nickels + pennies

def check_payment(drink_name, payment):
    """Checks the cost of the drink against payment received. Returns true if we've received enough."""

    return payment >= MENU[drink_name]['cost']

def make_coffee(drink_name):
    """Deducts the resources needed to make the requested drink."""

    ingredients = MENU[drink_name]['ingredients']

    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def coffee_machine():
    is_turned_on = True

    while is_turned_on:

        user_option = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_option == "report":
            print_report()
        elif user_option == "off":
            is_turned_on = False
        # process the drink 
        else:
            # only continue if we have enough resources
            if has_resources(user_option):

                payment = collect_coins()

                # only continue if we've received enough money
                if check_payment(user_option, payment):
                    # calculate change
                    change = round(payment - MENU[user_option]['cost'], 2)
                    # profit! 
                    resources['money'] += MENU[user_option]['cost']
                    
                    # make the drink
                    make_coffee(user_option)

                    # Give the stuff! 

                    print(f"Here is ${change} in change.")
                    print(f"Here is your {user_option}. Enjoy!")
                # otherwise refund the money
                else:
                    print(f"Sorry that's not enough money. Money refunded.")

coffee_machine()