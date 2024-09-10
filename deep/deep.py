

question = input(
"What's the answer to the Great Question of Life, the Universe and Everything? ")

if question.strip() == "42" :
    print ("Yes")
elif question.lower().strip() == "forty-two":
    print ("Yes")
elif question.lower().strip() == "forty two":
    print ("Yes")
else:
    print ("No")




