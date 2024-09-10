def main():
    message = input("Input: ")
    message_without_vowels = shorten(message)
    print("Output: " + message_without_vowels)

def shorten(words):
    words_without_vowels = ""
    for letters in words:
        if not letters.lower() in ['a','e','i','o','u']:
            words_without_vowels += letters
    return words_without_vowels


if __name__ == "__main__":
    main()