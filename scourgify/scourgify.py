import csv
import sys

# Check command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Try to open the input CSV file
try:
    with open(sys.argv[1], 'r') as input_file:
        reader = csv.DictReader(input_file)
        data = []

        # Reformat each row
        for row in reader:
            last, first = row["name"].split(", ")
            data.append({"first": first, "last": last, "house": row["house"]})

    # Write to the output CSV file
    with open(sys.argv[2], 'w') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(data)

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
