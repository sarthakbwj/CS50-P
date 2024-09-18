from fuel import convert, guage
import pytest

def main():
    test_correct_input()
    test_zero_division()
    test_value()

def test_correct_input():
    assert convert("1/4") == 25
    assert guage(25) == "25%"
    assert convert("1/100") == 1
    assert guage(1) == "E"
    assert convert("99/100") == 99
    assert guage(99) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")


if __name__ == "__main__":
    main()
