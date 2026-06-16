# PSEUDOCODE for Step6.py
# Concept: Validating input using while loops — keep asking until a valid answer is given

# BEGIN

    # IMPORT random number tools

    # --- BATTLE 1: Regular Enemy ---
    # PRINT "Your first enemy approaches. Prepare to battle!"

    # REPEAT forever:                             <-- while loop for input validation
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
    # ELSE
        # PRINT "The enemy defeated you. You died." in red
        # STOP the program
    # END IF


    # --- BATTLE 2: Boss Fight ---
    # PRINT "Boss battle! It's time to face Margit, the Fell Omen!"

    # REPEAT forever:                             <-- while loop for input validation
        # PROMPT user "Choose a number from 0 to 9"
        # SET enemy = user's answer
        # IF enemy is in the list ["0","1","2","3","4","5","6","7","8","9","uuddlrlrba"] THEN
            # BREAK out of loop                   <-- using 'in' list instead of many OR conditions
        # ELSE
            # PRINT "You did not enter a number from '0' to '9'."
        # END IF
    # END REPEAT

    # SET beast = random number from 0 to 9 (as text)

    # IF enemy equals beast OR enemy equals "uuddlrlrba" THEN
        # PRINT "You defeated the enemy!"
    # ELSE
        # PRINT "Margit has defeated you. You died." in red
    # END IF

# END
