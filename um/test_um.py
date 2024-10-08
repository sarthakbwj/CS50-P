from um import count

def main():
    test_upper_lower_case()
    test_word_with_um()
    test_surrounded_with_words()

def test_upper_lower_case():
    assert count("Um, thanks for the ablum.") == 1
    assert count("Um, thanks um...") == 2

def test_word_with_um():
    assert count('yummi') == 0

def test_surrounded_with_words():
    assert count('Hello um world') == 1
    assert count('um?') == 1


if __name__ == "__main__":
    main()