# create a dictionary with fruits and their calories.
fruits = {
    "apple":"130",
    "avocado":"50",
    "banana":"110",
    "cantaloupe":"50",
    "grapefruit":"60",
    "grapes":"90",
    "honeydew melon":"50",
    "kiwifruit":"90",
    "lemon":"15",
    "lime":"20",
    "nectarine":"60",
    "orange":"80",
    "peach":"60",
    "pear":"100",
    "pineapple":"50",
    "plum":"70",
    "strawberries":"50",
    "sweet cherries":"100",
    "tangerine":"50",
    "watermelon":"80",
}

# prompt the user for the input, make it case insensitive and strip whitespace if any.
item = input("Item: ").lower()


# use conditionals to check if the user input matches with the keys in the dictionary.
if item in fruits:
# if it matches print the "value" for the corresponding "key".
    print("Colories:",fruits[item])




