from plates import is_valid

def main():
    test_min_and_max_characters()
    test_must_start_with_two_letters()
    test_number_valid()
    test_number_zero()
    test_punctuations()


def test_min_and_max_characters():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFGH") == False
    assert is_valid("A") == False

def test_must_start_with_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_number_valid():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_number_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuations():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI 14") == False

if __name__ == "__main__":
    main()