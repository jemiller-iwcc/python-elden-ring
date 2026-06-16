# PSEUDOCODE for Step9.py
# Concept: Storing character data in a dictionary

# BEGIN

    # IMPORT random number tools

    # PROMPT user "What is your name, Tarnished?"
    # SET player_name = user's answer converted to lowercase

    # PRINT welcome message using player_name
    # PRINT "Please select a class, Tarnished:"
    # PRINT "Samurai"

    # PROMPT user to select a class
    # SET player_class = user's answer converted to lowercase

    # CREATE a dictionary called samurai with:
        # "type"   = "Samurai"
        # "hp"     = 10
        # "attack" = 20

    # PRINT "You selected the [samurai type]."
    # PRINT "Your starting HP is [samurai hp]."        <-- using string concatenation
    # PRINT "Your starting attack is [samurai attack]." <-- using f-string


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
