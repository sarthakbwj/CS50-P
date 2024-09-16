import sys

def main():
    command_line_arg()

    try: 
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:     
        sys.exit("File does not exist.")
    
    count_lines = 0
    # Loop through lines to check "#" or whitespace. 
    for line in lines:
        if not comment_or_whitespace(line):
            count_lines += 1
    print(count_lines)

# handel various inputs of the sys.argv from the user
def command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments.")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments.")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file.")

# Ignore whitespace and comments while counting lines of code. 
def comment_or_whitespace(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()
