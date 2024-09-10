# Ask for user input and store in a variable.
answer = input("Input: ")
# Print Output in one line
print("Output: ", end="")
# Iterate over the string using loops.
for letters in answer:
# Check for vowels.
    if not letters.lower() in ["a","e","i","o","u"]:
# print letters without vowels on the same line.
        print(letters, end="")
# print a newline to end cleanly.
print()
