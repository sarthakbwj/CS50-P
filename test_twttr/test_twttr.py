from twttr import shorten

def main():
    test_lower_upper_cases()
    test_numbers()
    test_punctuations()

def test_lower_upper_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwiTteR') == 'TeTtR'

def test_numbers():
    assert shorten("1234") == 1234

def test_punctuations():
    assert shorten("!?.,") == "!?.,"


if __name__ == "__main__":
    main() 