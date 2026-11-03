# ==========================================
# TRIAL 4: THE BUG HUNT
# ==========================================
# You played Branch Trials. Now the bugs from the game are hiding in REAL code.
#
# For EACH bug below:
#   1. PREDICT: before you run anything, write what you think it prints
#      next to "# PREDICTION:".
#   2. RUN the file and compare. Were you right?
#   3. FIX the code so it follows the rule in the story.
#   4. TEST: change the value at the top of the section to each of the
#      "Test with" values and run again. Your fix must work for ALL of them,
#      not just the first one.
#
# Hint: if a section prints the wrong thing, trace it the way Python does.
# Top to bottom, one True/False question at a time.


# BUG 1: The Upside-Down Ladder
# ------------------------------------------
# A 95 should get an A. Right now it gets a C.
# Test with: 95 -> A, 85 -> B, 75 -> C, 50 -> F
print("--- BUG 1 ---")
score = 95
# PREDICTION:

if score >= 70:
    print("C")
elif score >= 80:
    print("B")
elif score >= 90:
    print("A")
else:
    print("F")


# BUG 2: The Leaky Theme Park
# ------------------------------------------
# Rule: riders must be AT LEAST 12 years old AND AT LEAST 120 cm tall.
# Right now a tall 8-year-old gets on the ride.
# Test with: (8, 135) -> Not safe yet.   (12, 120) -> Strapping in!   (15, 119) -> Not safe yet.
print("--- BUG 2 ---")
age = 8
height = 135
# PREDICTION:

if age >= 12 or height >= 120:
    print("Strapping in!")
else:
    print("Not safe yet.")


# BUG 3: The Double Alarm
# ------------------------------------------
# The phone should show exactly ONE message:
#   under 10%  -> "Critical!"
#   under 30%  -> "Low battery"
#   otherwise  -> "All good"
# Right now 5% shows TWO messages, and 80% shows nothing at all.
# Test with: 5 -> Critical!   10 -> Low battery   25 -> Low battery   80 -> All good
print("--- BUG 3 ---")
battery = 5
# PREDICTION:

if battery < 30:
    print("Low battery")
if battery < 10:
    print("Critical!")


# BUG 4: The Off-By-One Sword
# ------------------------------------------
# Rule: the sword costs 100 coins. If you have AT LEAST 100 coins, you can buy it.
# A player with exactly 100 coins is complaining. Why?
# Test with: 99 -> Not enough coins.   100 -> Sword bought!   101 -> Sword bought!
print("--- BUG 4 ---")
coins = 100
# PREDICTION:

if coins > 100:
    print("Sword bought!")
else:
    print("Not enough coins.")


# BUG 5: The Health Bar That Never Ends
# ------------------------------------------
# At 0 HP the game should say "Game Over". It never does, no matter what.
# Test with: 0 -> Game Over   10 -> Danger!   60 -> Fighting
print("--- BUG 5 ---")
hp = 0
# PREDICTION:

if hp < 25:
    print("Danger!")
elif hp == 0:
    print("Game Over")
else:
    print("Fighting")

# QUESTION: Can the "Game Over" line EVER run in the original code? Why not?
# ANSWER:


# BUG 6: The Safe That Never Opens
# ------------------------------------------
# The PIN is 4321. Type 4321 when it asks... and the safe still won't open.
# It doesn't crash. It's just silently wrong, which is worse.
# Test with: 4321 -> Safe opens.   1234 -> Wrong PIN.
print("--- BUG 6 ---")
pin = input("Enter the 4-digit PIN: ")
# PREDICTION (when you type 4321):

if pin == 4321:
    print("Safe opens.")
else:
    print("Wrong PIN.")

# QUESTION: Why was 4321 not equal to 4321?
# ANSWER:


# ==========================================
# BOSS LEVEL: Build The Ticket Booth
# ==========================================
# No bugs to fix here. You write it from scratch.
# Ask the visitor for their age, then print their ticket:
#   - Kids UNDER 5 OR seniors 65 AND OLDER: "Free entry!"
#   - Kids 5 to 12:                         "Kids ticket: $5"
#   - Everyone else:                        "Regular ticket: $10"
#
# You'll need: int(input(...)), if / elif / else, and the word "or".
# Think about it: does the ORDER of your checks matter here? Try moving them around.
# Test with: 3, 5, 12, 13, 64, 65, 80

print("--- BOSS LEVEL ---")
# --- Write your code below ---
