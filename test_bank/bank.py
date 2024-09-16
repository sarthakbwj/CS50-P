
def main():
    greet = input("Greeting: ")
    amt = value(greet)
    print(f"${amt}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else: 
        return 100

if __name__ == "__main__":
    main()