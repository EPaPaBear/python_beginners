# ==========================================
# BRIDGE PROJECT 1: ARCADE HIGH SCORES
# ==========================================

# ------------------------------------------
# PHASE 1: The Data
# ------------------------------------------
# TODO 1: Create a list called 'high_scores'.
# Put three integer scores in it to start (e.g., 500, 300, 100).
high_scores = []

# ------------------------------------------
# PHASE 2: The Functions
# ------------------------------------------
def display_scores():
    print("\n=== TOP 5 HIGH SCORES ===")
    
    # TODO 2: Sort the list from highest to lowest.
    # Hint: high_scores.sort(reverse=True)
    
    
    # TODO 3: Create a FOR loop to print the scores.
    # We only want to print up to 5 scores!
    # Hint: We can slice the list in the loop: for score in high_scores[:5]:
    
    
    print("=========================")

def add_score():
    print("\n--- NEW GAME OVER ---")
    # TODO 4: Ask the user for their final score using input()
    # Remember to turn it into an integer using int()!
    
    
    # TODO 5: Use .append() to add their score to the high_scores list.
    
    
    print("Score saved!")

# ------------------------------------------
# PHASE 3: The Arcade Loop
# ------------------------------------------
print("Booting Arcade OS...")

# TODO 6: Create the 'while True' menu loop.
# 1. Print options: [1] Play Game (Add Score)  [2] View Leaderboard  [3] Unplug Machine
# 2. Get user choice.
# 3. Use IF/ELIF to call the right function.
# 4. If they choose [3], print a goodbye message and break the loop.