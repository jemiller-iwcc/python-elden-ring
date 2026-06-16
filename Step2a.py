# Introducing decision making with if statements!

# Variables in Python are named using what is called snake case, which means that all letters are lowercase and words are separated by underscores. This is just a convention, but it helps make your code more readable.

# If you want to accept either uppercase or lowercase letters, you can use the .lower() method to convert the input to lowercase before checking it.

elden_ring = input("Hey, do you like Elden Ring? (y/n): ").lower()

if elden_ring == "y":
    print("Great! Elden Ring is an amazing game!")
elif elden_ring == "n":
    print("Oh, that's too bad. Maybe you should give it a try!")
else:
    print("You did not enter \"y\" or \"n\". \033[91mYou died.\033[0m")