
# Take user input and store in variable "camelCase"
camelCase = input("camelCase: ")

# Initialize the "snake_case" to accumulate the formatted string.
snake_case = ""

# Iterate over each letter in the string.
for letters in camelCase:

# Check if the character is uppercase.
    if letters.isupper():

# If it is, replace Uppercase with "_" followed by lower case of the same string.
        snake_case += "_" + letters.lower()

    else:
# If not, print string as it is.
        snake_case += letters

print("snake_case: " , snake_case)
