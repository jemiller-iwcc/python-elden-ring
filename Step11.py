# Step 11: A fully realized game — classes, hit points, and attacks all matter now.
# This builds on everything from Steps 1-10: input, variables, dictionaries, loops,
# conditionals, and random. New here: functions, a real combat system, and a full game loop.

import random

# ANSI escape codes for terminal color — same technique used in Step 10 for "You Died."
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"


# ─────────────────────────────────────────────────────────────────────────────
#  FUNCTIONS  (new in Step 11 — we use them to avoid repeating the same logic)
# ─────────────────────────────────────────────────────────────────────────────

def show_hp_bar(current, maximum, label):
    """Print a colored HP bar for a combatant."""
    bar_length = 20
    filled = int(bar_length * current / maximum)
    bar = "█" * filled + "░" * (bar_length - filled)

    # Color shifts from green → yellow → red as HP drops
    if current > maximum * 0.5:
        color = GREEN
    elif current > maximum * 0.25:
        color = YELLOW
    else:
        color = RED

    print(f"  {label:35s} {color}[{bar}]{RESET} {current}/{maximum} HP")


def battle(player, enemy, flasks):
    """
    Run one complete fight between the player and an enemy.
    Returns the updated flask count (flasks can be spent during the fight).
    """
    label = f"BOSS: {enemy['name']}" if enemy.get("is_boss") else enemy["name"]
    header_color = YELLOW if enemy.get("is_boss") else RED
    print(f"\n{BOLD}{header_color}─── {label} ───{RESET}")
    print(enemy.get("intro", "An enemy approaches!"))
    print()

    enemy_hp     = enemy["hp"]
    enemy_max_hp = enemy["hp"]

    while True:
        # Show both HP bars every turn
        show_hp_bar(player["hp"], player["max_hp"], f"{player['type']} (You)")
        show_hp_bar(enemy_hp, enemy_max_hp, enemy["name"])

        # Build the action menu
        print("\n  What do you do?")
        print("  1. Attack")
        if flasks > 0:
            print(f"  2. Use Flask of Crimson Tears  ({CYAN}{flasks}{RESET} remaining)")

        action = input("  > ").strip().lower()
        print()

        # ── Resolve player action ──────────────────────────────────────────
        if action == "uuddlrlrba":
            # Easter egg: the cheat code from earlier steps becomes a secret power move
            cheat_damage = player["attack"] * 5
            enemy_hp -= cheat_damage
            print(f"{BOLD}{YELLOW}A mysterious power surges through you!{RESET}")
            print(f"You unleash {YELLOW}{cheat_damage}{RESET} damage in a blinding flash!")

        elif action == "1":
            variance = max(1, player["attack"] // 5)
            dmg = random.randint(player["attack"] - variance, player["attack"] + variance)
            enemy_hp -= dmg
            print(f"You strike for {YELLOW}{dmg}{RESET} damage!")

        elif action == "2" and flasks > 0:
            heal = int(player["max_hp"] * 0.4)
            player["hp"] = min(player["max_hp"], player["hp"] + heal)
            flasks -= 1
            print(f"You drink from your flask, recovering {GREEN}{heal}{RESET} HP!")

        else:
            print("You hesitate...")

        # ── Enemy counterattack (always fires unless the enemy just died) ──
        if enemy_hp > 0:
            variance = max(1, enemy["attack"] // 5)
            enemy_dmg = random.randint(enemy["attack"] - variance, enemy["attack"] + variance)
            player["hp"] -= enemy_dmg
            print(f"{enemy['name']} strikes back for {RED}{enemy_dmg}{RESET} damage!")

        print()

        # ── Check win/loss ─────────────────────────────────────────────────
        if enemy_hp <= 0:
            print(f"{GREEN}You defeated {enemy['name']}!{RESET}")
            return flasks

        if player["hp"] <= 0:
            print(f"{BOLD}{RED}You were overcome...{RESET}")
            print(f"\033[91mYOU DIED\033[0m")
            exit()


# ─────────────────────────────────────────────────────────────────────────────
#  GAME START
# ─────────────────────────────────────────────────────────────────────────────

player_name = input("What is your name, Tarnished? ").lower()
print(f"Welcome, {player_name.title()}! Your journey to become Elden Lord begins now!")

print("\nPlease select a class:")
print("  1. Samurai  — Balanced warrior           (HP:  80,  ATK: 25)")
print("  2. Prisoner — Glass cannon               (HP:  60,  ATK: 35)")
print("  3. Prophet  — Resilient, but slow        (HP: 100,  ATK: 15)")

while True:
    player_class = input("> ").strip()
    if player_class in ["1", "2", "3"]:
        break
    print("Please enter 1, 2, or 3.")

# Same dictionary structure as Step 10 — now the stats actually mean something
classes = {
    "1": {"type": "Samurai",  "hp": 80,  "max_hp": 80,  "attack": 25},
    "2": {"type": "Prisoner", "hp": 60,  "max_hp": 60,  "attack": 35},
    "3": {"type": "Prophet",  "hp": 100, "max_hp": 100, "attack": 15},
}

# .copy() makes a new dictionary so changes to player["hp"] during the game
# don't overwrite the original template inside classes.
player = classes[player_class].copy()
flasks = 2

print(f"\n{BOLD}You chose the {player['type']} class.{RESET}")
print(f"  HP: {GREEN}{player['hp']}{RESET}  |  ATK: {YELLOW}{player['attack']}{RESET}  |  Flasks: {CYAN}{flasks}{RESET}")


# ─────────────────────────────────────────────────────────────────────────────
#  ENEMY POOLS  (random.sample picks 2 unique enemies per act)
# ─────────────────────────────────────────────────────────────────────────────

regular_enemies = [
    {"name": "Wandering Noble",       "hp": 20,  "attack": 6,  "intro": "A frenzied noble lunges at you with a broken sword!"},
    {"name": "Godrick Foot Soldier",  "hp": 28,  "attack": 8,  "intro": "A Godrick foot soldier rushes forward!"},
    {"name": "Soldier of Godrick",    "hp": 35,  "attack": 10, "intro": "A heavily armored soldier blocks your path!"},
    {"name": "Godrick Knight",        "hp": 50,  "attack": 13, "intro": "A Godrick knight charges with lance leveled!"},
    {"name": "Giant Crab",            "hp": 60,  "attack": 11, "intro": "A monstrous crab erupts from the mud!"},
    {"name": "Troll",                 "hp": 75,  "attack": 16, "intro": "The earth trembles — a troll crashes through the treeline!"},
]

bosses = [
    {
        "name": "Margit, the Fell Omen",
        "hp": 90, "attack": 20,
        "intro": "A decrepit figure drops from the bridge above.\n  'Foul Tarnished — thy kind are denied the Elden Ring!'",
        "is_boss": True,
    },
    {
        "name": "Godrick the Grafted",
        "hp": 130, "attack": 26,
        "intro": "The grafted tyrant rises from his throne of corpses.\n  'I'll graft ye to me own flesh!'",
        "is_boss": True,
    },
    {
        "name": "Rennala, Queen of the Full Moon",
        "hp": 110, "attack": 22,
        "intro": "The amber egg fractures. Rennala descends, wreathed in moonlight and sorrow.",
        "is_boss": True,
    },
]


# ─────────────────────────────────────────────────────────────────────────────
#  GAME LOOP  — Three acts, each ending in a boss fight
# ─────────────────────────────────────────────────────────────────────────────

act_titles = ["Stormveil Castle", "Godrick's Domain", "The Academy of Raya Lucaria"]

print("\n" + "=" * 54)
print("  The Lands Between stretch before you...")
print("=" * 54)

for act_num, boss in enumerate(bosses, start=1):
    print(f"\n{BOLD}Act {act_num}: {act_titles[act_num - 1]}{RESET}")
    input("Press Enter to venture forth...\n")

    # Two random enemies drawn from the pool without repeats
    enemies_this_act = random.sample(regular_enemies, 2)
    for enemy in enemies_this_act:
        flasks = battle(player, enemy, flasks)

    # Boss fight caps each act
    flasks = battle(player, boss, flasks)

    # Site of Grace between acts (not after the final boss)
    if act_num < len(bosses):
        print(f"\n{BOLD}{YELLOW}★  A Site of Grace glows ahead...{RESET}")
        print("   Your wounds close. The road to the Elden Ring grows shorter.")
        player["hp"] = player["max_hp"]
        flasks = 2
        print(f"   HP restored to {GREEN}{player['hp']}{RESET}. Flasks refilled to {CYAN}{flasks}{RESET}.")
        input("\nPress Enter to continue...\n")


# ─────────────────────────────────────────────────────────────────────────────
#  VICTORY
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 54)
print(f"  {BOLD}{YELLOW}ELDEN LORD — {player_name.title()}{RESET}")
print("=" * 54)
print("\n  The Elden Ring is mended. The shattered world holds together once more.")
print(f"\n  Congratulations, {player_name.title()}. You are Elden Lord.\n")
