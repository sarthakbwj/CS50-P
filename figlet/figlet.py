import sys
from pyfiglet import Figlet 
import random

figlet = Figlet()

# Check command-line arguments
if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else: 
    print("Invalid Usage")
    sys.exit(1)

# Get all available fonts
all_fonts = figlet.getFonts()

# Set font based on input or randomize
if isRandomFont == False:
    if sys.argv[2] in all_fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        print("Invalid font")
        sys.exit(1)
else: 
    random_font = random.choice(all_fonts)
    figlet.setFont(font=random_font)

# Get input from the user
msg = input("Input: ")
print(f"Output: ")
print(figlet.renderText(msg))