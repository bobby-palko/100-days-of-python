from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

def main():
    
    is_on = True

    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while is_on:

        choice = input(f"What would you like? ({menu.get_items()}): ")

        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "off":
            is_on = False
        else:
            # search for the drink
            drink = menu.find_drink(choice)
            # make sure its exists
            if drink:
                # make sure we have the resources
                if coffee_maker.is_resource_sufficient(drink):
                    # and that we got enough money
                    if money_machine.make_payment(drink.cost):
                        # do it! 
                        coffee_maker.make_coffee(drink)

main()