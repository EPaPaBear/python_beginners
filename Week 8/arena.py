# ==========================================
# WEEK 7 PROJECT: THE ARENA (Object Interaction)
# ==========================================
import time
import random

# ------------------------------------------
# PHASE 1: The Blueprint
# ------------------------------------------
# We only need ONE blueprint, even though we will have a Player and an Enemy.
class Fighter:
    
    # TODO 1: Create the __init__ method.
    # It needs 3 parameters: self, name, and hp
    def __init__(self, name, hp):
        # TODO 2: Save name and hp to 'self'
        self.name = name
        self.hp = hp
        
        # TODO 3: Generate a random attack power for this specific object!
        # Set self.attack_power to a random integer between 10 and 25.
        # Hint: random.randint(10, 25)
        self.attack_power = random.randint(10, 25)

    # ------------------------------------------
    # PHASE 2: Object Interaction! (The Magic)
    # ------------------------------------------
    # TODO 4: Create the attack method. 
    # It takes TWO parameters: 'self' (the attacker), and 'target' (the object being attacked)
    def attack(self, target):
        print(f"\n🗡️  {self.name} lunges at {target.name}!")
        
        # TODO 5: The Interaction!
        # Subtract self.attack_power from the target's HP.
        # Syntax hint: target.hp = target.hp - self.attack_power
        
        
        print(f"💥 {target.name} takes {self.attack_power} damage! (HP left: {target.hp})")


# ------------------------------------------
# PHASE 3: Instantiating the Objects
# ------------------------------------------
print("=== WELCOME TO THE ARENA ===")

# TODO 6: Create the Player object. Name them, and give them 100 HP.
# player = Fighter(?, ?)


# TODO 7: Create the Boss object. Name it "Goblin King", and give it 80 HP.
# boss = 


print(f"Matchup: {player.name} (Atk: {player.attack_power}) VS {boss.name} (Atk: {boss.attack_power})")
input("\nPress ENTER to start the battle...")

# ------------------------------------------
# PHASE 4: The Battle Loop
# ------------------------------------------

# TODO 8: Create the game loop.
# We want this loop to run AS LONG AS both fighters have more than 0 HP.
# Hint: while player.hp > 0 and boss.hp > 0:
while True: # <-- Change this!
    
    # 1. Player Attacks Boss
    # TODO 9: Call the attack method on the player, and pass the boss as the target!
    # Syntax hint: player.attack(boss)
    
    
    time.sleep(1) # Dramatic pause
    
    # 2. Check if the boss died from that attack
    if boss.hp <= 0:
        print(f"\n🏆 {boss.name} has been defeated! {player.name} WINS!")
        break # Exit the loop!
        
    # 3. Boss Attacks Player
    # TODO 10: Call the attack method on the boss, passing the player as the target.
    
    
    time.sleep(1)
    
    # 4. Check if the player died
    if player.hp <= 0:
        print(f"\n💀 {player.name} has fallen... GAME OVER.")
        break