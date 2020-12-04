from art import logo

# Define our primary operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divive(x, y):
    return x / y

# Assigns the above functions to their matching operators
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divive,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))

    for sign in operations:
        print(sign)

    # Allows the user to continue calculating with the answer from the previous calculation
    still_calculating = True

    while still_calculating:

        operation_sign = input("Pick an operation: ")

        num2 = float(input("What's the next number? "))

        # We pull the function from the dictionary, and pass the values given to it to get an answer
        operation = operations[operation_sign]
        answer = operation(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, 'n' for a new calculation, or anything else to exit: ").lower()

        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            still_calculating = False
            calculator()
        else:
            still_calculating = False

calculator()