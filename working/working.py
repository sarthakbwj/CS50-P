import re

def main():
    print(convert(input("Hours: ")))


import re

def convert(s):
    # Adjusted regular expression to allow optional minutes more clearly
    iscorrectFormat = re.search(r"^([0-9]{1,2})(:([0-5][0-9]))? ([AP]M) to ([0-9]{1,2})(:([0-5][0-9]))? ([AP]M)$", s)
    
    if iscorrectFormat:
        pieces = iscorrectFormat.groups()
        hour1, minute1, am_pm1, hour2, minute2, am_pm2 = pieces[0], pieces[2], pieces[3], pieces[4], pieces[6], pieces[7]
        
        # Set default minutes to "00" if not provided
        minute1 = minute1 if minute1 is not None else "00"
        minute2 = minute2 if minute2 is not None else "00"
        
        if int(hour1) > 12 or int(hour2) > 12:
            raise ValueError
        
        first_time = new_format(hour1, minute1, am_pm1)
        second_time = new_format(hour2, minute2, am_pm2)
        
        return first_time + " to " + second_time
    else:
        raise ValueError
    

def new_format(hour, minute, am_pm):
    # Convert hour based on AM/PM
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:  # AM case
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    
    # Return the time in 24-hour format
    return f"{new_hour:02}:{minute}"


    

def new_format(hour, minute, am_pm):
    # Convert hour based on AM/PM
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:  # AM case
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    
    # Handle minute, set default to "00" if minute is empty
    if minute is None or minute == "":
        new_minute = "00"
    else:
        new_minute = minute
    
    # Return the time in 24-hour format
    return f"{new_hour:02}:{new_minute:02}"


if __name__ == "__main__":
    main()
