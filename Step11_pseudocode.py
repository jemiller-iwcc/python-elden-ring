# PSEUDOCODE for Step11.py
# Concept: Functions, a real combat system, and a full three-act game loop

# BEGIN

    # IMPORT random number tools
    # DEFINE color constants (RED, GREEN, YELLOW, CYAN, BOLD, RESET)


    # ── FUNCTION: show_hp_bar(current, maximum, label) ───────────────────────
    # Purpose: Print a visual HP bar for a combatant

    # FUNCTION show_hp_bar(current, maximum, label):
        # SET bar_length = 20
        # SET filled = number of filled blocks based on current/maximum ratio
        # BUILD bar string of filled blocks and empty blocks

        # IF current > 50% of maximum THEN
            # SET color = GREEN
        # ELSE IF current > 25% of maximum THEN
            # SET color = YELLOW
        # ELSE
            # SET color = RED
        # END IF

        # PRINT label, colored bar, and "current/maximum HP"
    # END FUNCTION


    # ── FUNCTION: battle(player, enemy, flasks) ───────────────────────────────
    # Purpose: Run one complete fight; return the updated flask count

    # FUNCTION battle(player, enemy, flasks):
        # PRINT enemy name and intro text

        # SET enemy_hp     = enemy's starting HP
        # SET enemy_max_hp = enemy's starting HP

        # REPEAT forever:
            # DISPLAY HP bar for player
            # DISPLAY HP bar for enemy

            # PRINT action menu:
            #   "1. Attack"
            #   "2. Use Flask" (only if flasks > 0)

            # PROMPT user for an action

            # IF action equals "uuddlrlrba" (cheat code) THEN
                # SET cheat_damage = player's attack × 5
                # SUBTRACT cheat_damage from enemy_hp
                # PRINT cheat code flavor text and damage dealt

            # ELSE IF action equals "1" (Attack) THEN
                # SET dmg = random number near player's attack stat
                # SUBTRACT dmg from enemy_hp
                # PRINT damage dealt

            # ELSE IF action equals "2" AND flasks > 0 (Use Flask) THEN
                # SET heal = 40% of player's max HP
                # ADD heal to player's current HP (capped at max)
                # SUBTRACT 1 from flasks
                # PRINT HP recovered

            # ELSE
                # PRINT "You hesitate..."
            # END IF

            # IF enemy_hp > 0 THEN
                # SET enemy_dmg = random number near enemy's attack stat
                # SUBTRACT enemy_dmg from player's HP
                # PRINT enemy's counterattack damage
            # END IF

            # IF enemy_hp <= 0 THEN
                # PRINT "You defeated [enemy name]!"
                # RETURN updated flasks count
            # END IF

            # IF player's HP <= 0 THEN
                # PRINT "You were overcome..."
                # PRINT "YOU DIED" in red
                # STOP the program
            # END IF

        # END REPEAT
    # END FUNCTION


    # ── GAME START ────────────────────────────────────────────────────────────

    # PROMPT user "What is your name, Tarnished?"
    # SET player_name = user's answer converted to lowercase
    # PRINT welcome message

    # PRINT class selection menu:
    #   "1. Samurai  — HP:  80, ATK: 25"
    #   "2. Prisoner — HP:  60, ATK: 35"
    #   "3. Prophet  — HP: 100, ATK: 15"

    # REPEAT forever:
        # PROMPT user to pick class 1, 2, or 3
        # IF answer is valid THEN
            # BREAK out of loop
        # END IF
    # END REPEAT

    # CREATE classes dictionary:
        # "1" → { type: "Samurai",  hp: 80,  max_hp: 80,  attack: 25 }
        # "2" → { type: "Prisoner", hp: 60,  max_hp: 60,  attack: 35 }
        # "3" → { type: "Prophet",  hp: 100, max_hp: 100, attack: 15 }

    # SET player = a copy of the chosen class entry
    # SET flasks = 2
    # PRINT player's chosen class, HP, ATK, and flask count


    # ── ENEMY POOLS ───────────────────────────────────────────────────────────

    # CREATE list of regular enemies (each with name, hp, attack, intro text):
        # Wandering Noble, Godrick Foot Soldier, Soldier of Godrick,
        # Godrick Knight, Giant Crab, Troll

    # CREATE list of bosses (each with name, hp, attack, intro text, is_boss flag):
        # Margit the Fell Omen, Godrick the Grafted, Rennala Queen of the Full Moon


    # ── THREE-ACT GAME LOOP ───────────────────────────────────────────────────

    # SET act_titles = ["Stormveil Castle", "Godrick's Domain", "The Academy of Raya Lucaria"]

    # PRINT opening scene text

    # FOR each boss (act 1, act 2, act 3):
        # PRINT act number and title
        # WAIT for player to press Enter

        # RANDOMLY PICK 2 unique enemies from the regular enemy list
        # FOR each of those 2 enemies:
            # CALL battle(player, enemy, flasks)
            # UPDATE flasks with the returned value
        # END FOR

        # CALL battle(player, boss, flasks)      <-- boss fight ends the act
        # UPDATE flasks with the returned value

        # IF this is not the last act THEN
            # PRINT "A Site of Grace glows ahead..."
            # RESTORE player HP to full
            # REFILL flasks to 2
            # PRINT restored HP and flask count
            # WAIT for player to press Enter
        # END IF

    # END FOR


    # ── VICTORY ───────────────────────────────────────────────────────────────

    # PRINT "ELDEN LORD — [player_name]"
    # PRINT "The Elden Ring is mended."
    # PRINT "Congratulations, [player_name]. You are Elden Lord."

# END
