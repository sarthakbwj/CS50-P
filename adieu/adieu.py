import inflect
p = inflect.engine()

names = []
while True:
    try:
        names.append(input("Names: "))
    except EOFError:
        print()
        break

output = p.join(names)
print(f"Adieu, adieu, to "+ output)