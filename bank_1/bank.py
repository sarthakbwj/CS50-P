def main():

    greet = input ("Greeting: ").lower().strip()
    if greet.startswith("hello"):
        print("$0")
    elif greet[0] == "h":
        print("$20")
    else:
        print("$100")

main()
