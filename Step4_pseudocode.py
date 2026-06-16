# PSEUDOCODE for Step4.py
# Concept: Two battles — a regular enemy then a boss fight

# BEGIN

    # IMPORT random number tools

    # --- BATTLE 1: Regular Enemy ---
    # PRINT "Your first enemy approaches. Prepare to battle!"
    # PROMPT user "Choose a number, either 0 or 1"
    # SET enemy = user's answer (as text)
    # SET beast = random number, either 0 or 1 (as text)

    # IF enemy equals beast THEN
        # PRINT "You defeated the enemy!"
    # ELSE
        # PRINT "The enemy defeated you. You died." in red
    # END IF


    # --- BATTLE 2: Boss Fight ---
    # PRINT "Boss battle! It's time to face Margit, the Fell Omen!"
    # PROMPT user "Choose a number, either 0 or 9"
    # SET enemy = user's answer (as text)      [reusing same variable]
    # SET beast = random number from 0 to 9 (as text)

    # IF enemy equals beast THEN
        # PRINT "You defeated the enemy!"
    # ELSE
        # PRINT "Margit has defeated you. You died." in red
    # END IF

# END
