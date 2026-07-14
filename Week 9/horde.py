# ==========================================
# WEEK 8 PROJECT: ENTITY MANAGEMENT (THE HORDE)
# ==========================================
import time
import random

# ------------------------------------------
# PHASE 1: The Blueprints
# ------------------------------------------
class Zombie:
    def __init__(self, name):
        self.name = name
        self.hp = 30
        self.attack_power = 5

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print(f"💀 {self.name} has been destroyed!")

class Mage:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def cast_aoe_spell(self, enemy_list):
        print(f"\n✨ {self.name} casts FIREBALL on the entire horde! ✨")
        
        # TODO 1: Write a FOR loop to iterate through the 'enemy_list'.
        # For every 'zombie' in the list, call their take_damage method (e.g. 15 damage).
        
        


# ------------------------------------------
# PHASE 2: Building the Ecosystem
# ------------------------------------------
print("=== WELCOME TO THE WASTELAND ===")

# Instantiate the Player
hero = Mage("Gandalf")

# TODO 2: Create an empty list called 'horde'.
# horde = 


# TODO 3: Use a FOR loop and the range() function to instantly spawn 3 Zombies 
# and .append() them to the horde list!
# Hint: for i in range(3):
#           new_zombie = Zombie(f"Zombie {i}")
#           ...append it here...


print(f"Alert! A horde of {len(horde)} zombies is approaching!")
input("Press ENTER to begin combat...\n")


# ------------------------------------------
# PHASE 3: The Combat Loop
# ------------------------------------------
while hero.hp > 0:
    
    # 1. Player Attacks First
    # Call the hero's AoE spell, and pass the 'horde' list into it as the argument!
    hero.cast_aoe_spell(horde)
    time.sleep(1)
    
    # 2. Cleanup: Remove dead zombies from the list
    # (We use a clever trick here: list comprehension to keep only living zombies)
    horde = [z for z in horde if z.hp > 0]
    
    # 3. Check for victory
    if len(horde) == 0:
        print("\n🏆 The horde has been defeated! You win!")
        break
        
    # 4. The Horde Attacks Back!
    print("\n🧟 The horde strikes back!")
    
    # TODO 4: Write a FOR loop to iterate through the surviving 'horde'.
    # Every zombie gets to attack the hero!
    # Subtract the zombie's self.attack_power from the hero.hp.
    
    
    
    print(f"🛡️ Hero HP is now: {hero.hp}")
    time.sleep(2)
    
    # 5. Check for defeat
    if hero.hp <= 0:
        print("\n💀 You were overwhelmed by the horde. GAME OVER.")