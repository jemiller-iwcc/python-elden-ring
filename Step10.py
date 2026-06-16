# One class is awfully boring, so let's add a couple more.

import random

# Let's find out who you are.
player_name = input("What is your name, Tarnished? ").lower()

# Let's start simple, only one class at first. We will add more classes later on.
print("Welcome, " + player_name.title() + "! Your journey to become Elden Lord begins now!")
print("Please select a class, Tarnished. Choose a number:")
print("1. Samurai")
print("2. Prisoner")
print("3. Prophet")

# Don't forget to use the while loop to make sure the player enters a valid class number. We want to make sure they enter "1", "2", or "3". If they enter something else, we will keep asking them until they enter a valid number.
while True:
    player_class = input("> ")
    if player_class in ["1", "2", "3"]:
        break
    else:
      print("You did not enter a valid class number.")

# In Step 9, had a single variable holding just the stats of the Samurai. Now we can have one dictionary with multiple entries for each class. Each entry will be a dictionary itself, holding the stats for that class. This way, we can easily add more classes in the future by just adding more entries to the main dictionary.

classes = {
    "1": {"type": "Samurai", "hp": 10, "attack": 20},
    "2": {"type": "Prisoner", "hp": 20, "attack": 4},
    "3": {"type": "Prophet", "hp": 30, "attack": 4}
}

# Now that we have it in there, what do we do with it?
print("You selected the " + classes[player_class]["type"] + " class.") # We have used something called concatenation to combine multiple objects into a single string. This will show in the terminal "You have selected the Samurai."
print("Your starting HP is " + str(classes[player_class]["hp"]) + ".") # We have to use the str() function to convert the integer value of hp to a string so that we can concatenate it with the other strings. This will show in the terminal "Your starting HP is 10."
print(f"Your starting attack is {classes[player_class]['attack']}.") # Notice with the f-string, we did not need to convert the value 4 to a sting first. This will show in the terminal "Your starting attack is 4."

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
    