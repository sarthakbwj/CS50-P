def main():
    fraction = input("Fraction: ")    
    convert_fraction = convert(fraction)
    output = guage(convert_fraction)
    print(output)

def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)
            z = x/y
            if z <= 1:
                a = int(z*100)
                return a 
            else:
                fraction = input()
                pass    
        except (ValueError, ZeroDivisionError):
            raise

def guage(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()