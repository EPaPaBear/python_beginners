# ==========================================
# TRIAL 1: THE INFINITE LOOP TRAP
# ==========================================
# The script below is trying to "brute force" a 4-digit PIN by counting down from 5.
# 1. Run it. Watch it crash your terminal by running forever.
# 2. Click inside the terminal and press Ctrl + C to force stop it.
# 3. Fix the bug so it actually counts down to 0 and stops.

attempts_left = 5

print("--- COMMENCING BRUTE FORCE ---")

while attempts_left > 0:
    print("Trying PIN... Attempts remaining:", attempts_left)
    
    # TODO: The loop is stuck because attempts_left never changes!
    # Write code here to subtract 1 from attempts_left every time the loop runs.
    
    

print("System Locked. Brute force failed.")