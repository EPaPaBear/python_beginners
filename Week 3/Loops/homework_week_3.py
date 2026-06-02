# ==========================================
# WEEK 3 CHALLENGES
# ==========================================

# CHALLENGE 1: The Decryptor
# ------------------------------------------
# You received the encrypted message: "kdfnhu"
# We know it was shifted FORWARD by 3. 
# Write a script using a for loop, ord(), and chr() to shift it BACKWARDS by 3 
# and print the original message.

encrypted_data = "kdfnhu"
decrypted_data = ""

# --- Write Challenge 1 below ---




# CHALLENGE 2: Fixing the "Z" Bug (The Wrap-Around)
# ------------------------------------------
# In class, we learned that shifting "z" by 3 turns it into "}". 
# We want it to wrap around back to the start of the alphabet (z -a -b -c).
#
# Write a new shift loop for the word "zebra".
# Inside your loop, use an IF statement: 
# IF the new ASCII number goes higher than 122 (which is 'z'):
#    Subtract 26 from the number to force it back to the start of the alphabet.
# ELSE:
#    Just keep the number as is.
# Finally, turn it into a character and add it to your final string.

word = "zebra"
fixed_encryption = ""

# --- Write Challenge 2 below ---