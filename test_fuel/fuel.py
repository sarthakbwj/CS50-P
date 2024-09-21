def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        return round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
