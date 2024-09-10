def main():
    plate = input("Enter a vanity plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (is_length_valid(s) and
            starts_with_two_letters(s) and
            is_alphanumeric(s) and
            are_numbers_at_end(s) and
            is_first_number_nonzero(s))

def is_length_valid(s):
    return 2 <= len(s) <= 6

def starts_with_two_letters(s):
    return len(s) > 1 and s[0].isalpha() and s[1].isalpha()

def is_alphanumeric(s):
    return s.isalnum()

def are_numbers_at_end(s):
    number_found = False
    for char in s:
        if char.isdigit():
            number_found = True
        elif number_found:
            return False
    return True

def is_first_number_nonzero(s):
    for char in s:
        if char.isdigit():
            return char != '0'
    return True

if __name__ == "__main__":
    main()
