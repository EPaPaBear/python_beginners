# ==========================================
# EXERCISE 1: THE DETECTIVE (DEBUGGING)
# ==========================================
# The Problem: A junior engineer wrote this spaceship launch sequence, 
# but it keeps crashing. 
#
# YOUR MISSION: 
# Run the code. Read the red error messages. Fix the bugs ONE BY ONE 
# until the ship launches successfully. Do NOT rewrite the whole thing!

def run_diagnostics():
    print("Running system diagnostics...")
    systems = ["Engine", "Life Support", "Navigation"]
    
    # BUG 1: The system is trying to check a 4th item that doesn't exist.
    # Hint: Remember how lists are numbered!
    print("Checking: " + systems[0])
    print("Checking: " + systems[1])
    print("Checking: " + systems[2])
    print("Checking: " + systems[3]) 

def initiate_countdown():
    # BUG 2: This loop is supposed to count down from 5 to 1, but it goes forever!
    # Hint: What did the junior engineer forget to do to 'timer'?
    timer = 5
    while timer > 0:
        print(f"T-Minus: {timer}...")
        
    print("Liftoff!")

def verify_fuel():
    fuel_level = "100"
    
    # BUG 3: A TypeError. We are trying to do math with a String!
    # Hint: How do we convert text to a number?
    if fuel_level > 50:
        print("Fuel levels optimal.")
    else:
        print("Warning: Low Fuel.")


# --- MAIN PROGRAM ---
print("--- SPACESHIP LAUNCH SEQUENCE ---")
# BUG 4: A SyntaxError. Something is missing at the end of this if-statement.
if True
    run_diagnostics()
    verify_fuel()
    initiate_countdown()