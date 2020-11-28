# Tip calculator

# Greeting
print("Welcome to the tip calculator.")

# Prompt for bill amount
bill = float(input("What was the total bill? $"))

# Prompt for tip percentage
tip = int(input("What percentage tip would you like to give? "))

# Splitting the bill?
ways_to_split = int(input("How many people are splitting the bill? "))

# Figure out the total amount
total_amount = bill + (bill * (tip/100))

# Calculate how much each person should pay
individual_amount = total_amount / ways_to_split

# Print the results, rounding the amount to 2 decimal places for currency
print(f"Each person should pay: ${round(individual_amount, 2)}")