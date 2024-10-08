from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_day = input("Date of Birth: ")
    try:
        year,month,day = check_birthday(birth_day)
    except:
        sys.exit("Invalid Date")

    date_of_birth = date(int(year), int(month), int(day))
    date_of_today = date.today()
    diff = date_of_today - date_of_birth
    total_minutes = diff.days * 24 * 60
    output = p.number_to_words(total_minutes, andword="")
    print (output.capitalize()+ " minutes")

def check_birthday(birth_day):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_day):
        year,month,day = birth_day.split("-")
        return year,month,day 


if __name__ == "__main__":
    main()