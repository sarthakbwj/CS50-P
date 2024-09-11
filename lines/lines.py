import sys

def main():
    command_line_arg()

    try: 
        file = open(sys.argv[1],"r")
        lines = (file.readlines())
        print(lines)
    except FileNotFoundError:     
        sys.exit("File does not exist.")

def command_line_arg():
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments.")

        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments.")

        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file.")

if __name__ == "__main__":
    main()



