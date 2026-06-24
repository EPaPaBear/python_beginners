# ==========================================
# WEEK 5 PROJECT: THE TERMINAL TAMAGOTCHI (STARTER)
# ==========================================
import time
import random

# ------------------------------------------
# PHASE 1: The State (Data Structures)
# ------------------------------------------
# TODO 1: Complete the pet_stats dictionary.
# It needs 4 more keys: "hunger", "boredom", "energy" (set them all to 50) 
# and "is_alive" (set to True).
pet_stats = {
    "name": "Glitch",
    
}

# ------------------------------------------
# PHASE 2: The UI (Functions)
# ------------------------------------------
def print_status():
    """Prints the current state of the pet visually."""
    print("\n" + "="*30)
    print(f"[*] {pet_stats['name']}'s Status [*]")
    print("="*30)
    # TODO 2: Write three print statements to show Hunger, Boredom, and Energy.
    # Make sure to extract the values from the pet_stats dictionary!
    
    
    
    print("="*30)

# ------------------------------------------
# PHASE 3: The Actions (Modifying State)
# ------------------------------------------
def feed_pet():
    print(f"\n> You fed {pet_stats['name']} a digital byte!")
    # TODO 3: Decrease the pet's hunger by 20.
    
    # TODO 4: Increase the pet's energy by 10.
    
    
    # Logic check: Don't let hunger go below 0!
    if pet_stats["hunger"] < 0:
        pet_stats["hunger"] = 0

def play_with_pet():
    print(f"\n> You played a mini-game with {pet_stats['name']}!")
    # TODO 5: Decrease boredom by 30.
    
    # TODO 6: Decrease energy by 20. (Playing makes them tired!)
    
    
    if pet_stats["boredom"] < 0:
        pet_stats["boredom"] = 0

def put_to_sleep():
    print(f"\n> {pet_stats['name']} goes into sleep mode... Zzz...")
    # TODO 7: Set energy back to 100.
    
    # TODO 8: Increase hunger by 20 (sleeping makes you hungry!)
    
    time.sleep(2) # Pause the program for 2 seconds

# ------------------------------------------
# PHASE 4: The Game Loop & Time Mechanics
# ------------------------------------------
def check_health():
    """Checks if the pet has died from neglect."""
    # TODO 9: Write the IF statement.
    # IF hunger is >= 100 OR boredom is >= 100 OR energy is <= 0:
    #   Set the dictionary's "is_alive" to False
    #   Print a Game Over message
    pass # Remove 'pass' when you write your code


# --- THE MAIN PROGRAM ---
print("Booting Tamagotchi OS...")
time.sleep(1)

# TODO 10: Make this loop run as long as the pet's "is_alive" status is True
while True: # <-- Change this condition!
    print_status()
    
    print("\nActions: [1] Feed  [2] Play  [3] Sleep  [4] Quit")
    choice = input("What do you want to do? ")
    
    # TODO 11: Write the IF/ELIF statements to handle the user's choice.
    # If choice is "1", call the feed_pet() function.
    # If choice is "2", call play_with_pet().
    # If choice is "3", call put_to_sleep().
    # If choice is "4", break the loop.
    
    
    
    # After every action, the pet naturally degrades
    pet_stats["hunger"] += random.randint(5, 15)
    pet_stats["boredom"] += random.randint(5, 15)
    pet_stats["energy"] -= random.randint(5, 10)
    
    # Ensure stats don't go over 100
    if pet_stats["hunger"] > 100: pet_stats["hunger"] = 100
    if pet_stats["boredom"] > 100: pet_stats["boredom"] = 100
    
    check_health()
    time.sleep(1)