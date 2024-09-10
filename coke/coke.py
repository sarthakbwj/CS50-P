# Initialize the total amount due
amount_due = 50

# Run a while loop until the amount due is fully paid off
while amount_due > 0:
    # Print the current amount due
    print("Amount Due:", amount_due)

    # Prompt the user to insert a coin and store it in the variable "coins"
    coins = int(input("Insert Coin: "))

    # Check if the inserted coin is one of the accepted denominations (25, 10, or 5 cents)
    if coins in [25, 10, 5]:
        # If the coin is accepted, subtract its value from the amount due
        amount_due -= coins

# Print the amount of change due
print("Change Owed:", abs(amount_due))
