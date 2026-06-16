# PSEUDOCODE for Step10.py
# Concept: A dictionary of dictionaries — multiple classes with their own stats

# BEGIN

    # IMPORT random number tools

    # PROMPT user "What is your name, Tarnished?"
    # SET player_name = user's answer converted to lowercase

    # PRINT welcome message using player_name
    # PRINT "Please select a class. Choose a number:"
    # PRINT "1. Samurai"
    # PRINT "2. Prisoner"
    # PRINT "3. Prophet"

    # REPEAT forever:
        # PROMPT user to pick a class number
        # SET player_class = user's answer
        # IF player_class is in ["1", "2", "3"] THEN
            # BREAK out of loop
        # ELSE
            # PRINT "You did not enter a valid class number."
        # END IF
    # END REPEAT

    # CREATE a dictionary called classes with entries for each class number:
        # "1" → { "type": "Samurai",  "hp": 10, "attack": 20 }
        # "2" → { "type": "Prisoner", "hp": 20, "attack":  4 }
        # "3" → { "type": "Prophet",  "hp": 30, "attack":  4 }

    # LOOK UP the chosen class inside the dictionary using player_class
    # PRINT "You selected the [class type]."
    # PRINT "Your starting HP is [class hp]."
    # PRINT "Your starting attack is [class attack]."


    # --- BATTLE 1: Regular Enemy ---
    # PRINT "Your first enemy approaches. Prepare to battle!"

    # REPEAT forever:
        # PROMPT user "Choose a number, either 0 or 1"
        # SET enemy = user's answer
        # IF enemy equals "0" OR "1" OR "uuddlrlrba" THEN
            # BREAK out of loop
        # ELSE
            # PRINT "You did not enter '0' or '1'."
        # END IF
    # END REPEAT

    # SET beast = random number, either 0 or 1 (as text)

    # IF enemy equals beast OR enemy equals "uuddlrlrba" THEN
        # PRINT "You defeated the enemy!"
    # ELSE IF player_name equals "your_name" THEN
        # PRINT "You survived by using elif statements!"
    # ELSE
        # IF player_name equals "justin" THEN
            # PRINT "You should have died, but you're awesome, so you survived!"
        # ELSE
            # PRINT "The enemy defeated you. You died." in red
            # STOP the program
        # END IF
    # END IF


    # --- BATTLE 2: Boss Fight ---
    # PRINT "Boss battle! It's time to face Margit, the Fell Omen!"

    # REPEAT forever:
        # PROMPT user "Choose a number from 0 to 9"
        # SET enemy = user's answer
        # IF enemy is in list of valid inputs THEN
            # BREAK out of loop
        # ELSE
            # PRINT "You did not enter a number from '0' to '9'."
        # END IF
    # END REPEAT

    # SET beast = random number from 0 to 9 (as text)

    # IF enemy equals beast OR enemy equals "uuddlrlrba" THEN
        # PRINT "You defeated the enemy!"
    # ELSE IF player_name equals "your_name" THEN
        # PRINT "You survived by using elif statements!"
    # ELSE
        # IF player_name equals "justin" THEN
            # PRINT "You should have died, but you're awesome, so you survived!"
        # ELSE
            # PRINT "Margit has defeated you. You died." in red
            # STOP the program
        # END IF
    # END IF

# END
