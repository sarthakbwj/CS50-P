# load the dictionary provided in the question.
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# initialize the variable "total_amount" to 0.
total_amount = 0

# use a forever loop with Boolean value as True.
while True:
    # Use try and except block.
    try:
        # take user input and store in variable item, titalize the user input.
        item = input("Item: ").title()
        # if user input matches to a key in dictionary...
        if item in menu:
            # store that value in variable "total_amount"
            total_amount += menu[item]
            # print the total amount
            print ("Total: $",end="")
            # use 2 decimal points in the value.
            print("{:.2f}".format(total_amount))
# use except block to catch "End of File errors".
    except EOFError:
        # if found, break loop. 
        break

