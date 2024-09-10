
# ask for user input.
a = (input("Expression: "))

# split the input into 3 variables.
x, y, z = (a).split(" ")

# convert the variables to floats from strings. No need to create new variables.
x = float(x)
z = float(z)

# use the if conditionals to go through all the possible user inputs and
# build a case for it. No need of the catch all "_" here as the user limits are defined.

if y == "+":
        add = x + z
        print(add)
if y == "-":
        sub = x - z
        print(sub)
if y == "*":
        mul = x * z
        print(mul)
if y == "/":
        div = x / z
        # round the answer to 2 decimal points.
        rnd = round(div, 2)
        print(rnd)











