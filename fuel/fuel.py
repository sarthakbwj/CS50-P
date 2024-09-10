# Use a while loop to initialize the code and set its value as True.
while True:
    # Use the try block and try getting the integer,slash,integer as the input and store in a variable.
    try:
        fraction = input("Fraction: ")
        # Split the variable and store the input in seperate variables.
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        # Divide the variables x and y. Store the result in variable z.
        z = x/y
        # Use an if block to set the upper limit of the division as 1 or 100%.
        if z <= 1:
            # Use the break statement to break out of the loop and continue.
            break
        # Use except block to handel the Value Errors and Zero Division Errors from user's input.
    except (ValueError, ZeroDivisionError):
        pass

# Convert the float into int and store in a variable.
fract = round(z*100)
# Use conditionals.
if fract >= 99:
    print("F")
elif fract <= 1:
    print("E")
else:
    print(fract,"%",sep="")








