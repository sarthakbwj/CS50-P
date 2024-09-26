import sys
import csv

def main():
    check_correct_args()
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("CSV couldn't read CSV file")

    output = []
    for row in data:
        stream = select_stream(row["subject"])  
        year = select_birthyear(row["birthyear"])  
        output.append({"name": row["name"], "stream": stream, "year": year})  

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "stream", "year"])  
        writer.writeheader()  
        for row in output:
            writer.writerow(row)

def check_correct_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV files")

def select_stream(sub):
    if sub in ["Mathematics", "Computer Science", "Astronomy", "Engineering", "Earth Science", "Physics", "Chemistry"]:
        return "Science"
    elif sub in ["Insurance", "Finance", "Banking", "Company Secretary", "Accountant"]:
        return "Commerce"
    elif sub in ["History", "Geography", "Linguistics", "Sociology", "Philosophy"]:
        return "Arts"
    else:
        return "No Stream"

def select_birthyear(year):
    age = 2024 - int(year)
    grade = age - 18
    return "Year " + str(grade)

if __name__ == "__main__":
    main()
