from numb3rs import validate

def main():
    test_format()
    test_number_range()


def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2.") == False
    assert validate(r"1") == False

def test_number_range():
    assert validate(r"509.1.1.1") == False
    assert validate(r"1.509.1.1") == False
    assert validate(r"1.1.509.1") == False
    assert validate(r"1.1.1.509") == False

if __name__== "__main__":
    main()