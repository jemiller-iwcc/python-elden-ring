# PSEUDOCODE for Step7.py
# Concept: Nested if statements — a special player name can survive death

# BEGIN

    # IMPORT random number tools

    # PROMPT user "What is your name, Tarnished?"
    # SET player_name = user's answer converted to lowercase


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
    # ELSE                                        <-- nested if: special name bypass
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
    # ELSE                                        <-- same nested name check for boss
        # IF player_name equals "justin" THEN
            # PRINT "You should have died, but you're awesome, so you survived!"
        # ELSE
            # PRINT "Margit has defeated you. You died." in red
            # STOP the program
        # END IF
    # END IF

# END
