# ==========================================
# TRIAL 2: THE BOUNCER'S TRAP
# ==========================================
# The Bouncer checks if you are old enough to play an M-Rated (17+) video game.
# The code below crashes when you run it and type a number. 
# 1. Run it and watch it fail. Read the TypeError.
# 2. Fix the code so the Bouncer can successfully do the math.
# Hint: Look at your cheat sheet's section on input()!

user_age = input("Bouncer: How old are you? ")

# TODO: Fix the bug causing the line below to crash.
if user_age >= 17:
    print("Bouncer: You're good to go. Enjoy the game.")
else:
    print("Bouncer: Sorry kid, come back in a few years.")
