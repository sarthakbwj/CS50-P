import sys
import csv
from tabulate import tabulate

def main():
    command_line_arg()
    table = []
    try:
        with open(sys.argv[1],"r") as csvfile: 
            reader = csv.reader(csvfile)
            for line in reader:
                table.append(line)

    except FileNotFoundError:
        sys.exit("File does not exist.")

    print(tabulate(table[1:], headers= table[0], tablefmt= "grid"))

def command_line_arg():
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file.")

if __name__ == "__main__":
    main()