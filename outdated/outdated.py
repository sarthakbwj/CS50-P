months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

while True:
    date = input("Date: ")

    try:
        # Format: Month Day, Year
        if "," in date:
            month, day, year = date.replace(",", "").split()
            if int(day) <= 31:
                print(f"{year}-{months[month]}-{int(day):02}")
                break

        # Format: MM/DD/YYYY
        else:
            month, day, year = date.split("/")
            if int(month) <= 12 and int(day) <= 31:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break

    except ValueError:
        pass
