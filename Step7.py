# Let's see if anyyone can win this by just being awesome using some nested logic.

import random

# Let's find out who you are.
player_name = input("What is your name, Tarnished? ").lower() # The .lower() method is used to convert the input to lowercase. This way, we can accept either uppercase or lowercase letters and it will still work. For example, if the player enters "Justin", it will be converted to "justin". If they enter "JUSTIN", it will also be converted to "justin". This makes our code more flexible and user-friendly.


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
else:
    if player_name == "justin":
        print("You should have died, but you're awesome, so you survived!")
    else:
        print("Margit has defeated you. \033[91mYou died.\033[0m")
        exit()
    