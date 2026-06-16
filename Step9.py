# Let's add a class using dictionaries!

import random

# Let's find out who you are.
player_name = input("What is your name, Tarnished? ").lower() # The .lower() method is used to convert the input to lowercase. This way, we can accept either uppercase or lowercase letters and it will still work. For example, if the player enters "Justin", it will be converted to "justin". If they enter "JUSTIN", it will also be converted to "justin". This makes our code more flexible and user-friendly.

# Let's start simple, only one class at first. We will add more classes later on.
print("Welcome, " + player_name.title() + "! Your journey to become Elden Lord begins now!")
print("Please select a class, Tarnished:")
print("Samurai")

player_class = input("> ").lower()

samurai = {
    "type": "Samurai",
    "hp": 10,
    "attack": 20
}

# Now that we have it in there, what do we do with it?
print("You selected the " + samurai["type"] + ".") # We have used something called concatenation to combine multiple objects into a single string. This will show in the terminal "You have selected the Samurai."
print("Your starting HP is " + str(samurai["hp"]) + ".") # We have to use the str() function to convert the integer value of hp to a string so that we can concatenate it with the other strings. This will show in the terminal "Your starting HP is 10."
#This is an alternative method of concatenation called an f-string. It allows us to embed expressions inside string literals, using curly braces {}. This can make our code more readable and easier to write. For example, we could write:
print(f"Your starting attack is {samurai['attack']}.") # Notice with the f-string, we did not need to convert the value 20 to a string first. This will show in the terminal "Your starting attack is 20."

# Either method, be it f-strings or concatenation, is fine. You can use whichever one you prefer. The important thing is that you understand how to use both methods and when to use them. In general, f-strings can make your code more readable and easier to write, especially when you have multiple variables to include in the string. Concatenation can be useful for simple cases or when you want to include a lot of static text in the string.

print("Your first enemy approaches. Prepare to battle!")
while True:
    enemy = input("Choose a number, either 0 or 1: ")
    if enemy == "0" or enemy == "1" or enemy =="uuddlrlrba":
        break
    else:
      print("You did not enter \"0\" or \"1\".") 
        
beast = str(random.randint(0, 1))

if enemy == beast or enemy =="uuddlrlrba":
    print("You defeated the enemy!")
elif player_name == "your_name": # Replace "your_name" with your actual name in lowercase. For example, if your name is Bob, you would write player_name == "bob".
    print("You should have died, but you're awesome and learned how to use elif statements, so you survived!")
else:
    if player_name == "justin":
        print("You should have died, but you're awesome, so you survived!")
    else:
        print("The enemy defeated you. \033[91mYou died.\033[0m")
        exit()
    

print("Boss battle! It's time to face Margit, the Fell Omen!")
    
while True:
    enemy = input("Choose a number from 0-9: ")
    if enemy in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "uuddlrlrba"]:
        break
    else:
      print("You did not enter a number from \"0\" to \"9\".")
           
beast = str(random.randint(0, 9)) 

if enemy == beast or enemy =="uuddlrlrba":
    print("You defeated the enemy!")
elif player_name == "your_name": # Replace "your_name" with your actual name in lowercase. For example, if your name is Bob, you would write player_name == "bob".
    print("You should have died, but you're awesome and learned how to use elif statements, so you survived!")
else:
    if player_name == "justin":
        print("You should have died, but you're awesome, so you survived!")
    else:
        print("Margit has defeated you. \033[91mYou died.\033[0m")
        exit()
    