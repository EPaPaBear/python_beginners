# ==========================================
# ARC 1 FINALE: THE COMPILER
# ==========================================
# Python has a built-in bin() function. We aren't using it.
# You are going to write the actual math algorithm to convert a normal number into Binary.
#
# THE ALGORITHM RULES (Decimal to Binary):
# 1. Divide the number by 2.
# 2. Keep the REMAINDER (which will always be 1 or 0). That is your bit!
# 3. Add that bit to the FRONT of your binary string.
# 4. Update your number by cutting it in half (ignoring decimals).
# 5. Repeat until the number hits 0.

print("--- DECIMAL TO BINARY ENGINE ---")

# We start with a test number and an empty string to hold our bits.
target_number = 13
binary_output = ""

print(f"Converting the number: {target_number}")

# TODO: Build the converter loop.
# 1. Create a while loop that runs as long as target_number is greater than 0.
# 2. Inside the loop, find the remainder using modulo: target_number % 2
# 3. Convert that remainder to a string and add it to the FRONT of binary_output.
#    (Hint: binary_output = str(remainder) + binary_output)
# 4. Cut the target_number in half using floor division: target_number // 2

# --- Write your loop below ---



# --- Do not change the code below ---
print(f"Final Binary String: {binary_output}")
print(f"To check your work, Python says: {bin(13)}")