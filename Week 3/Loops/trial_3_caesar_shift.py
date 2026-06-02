# ==========================================
# TRIAL 3: THE CAESAR CIPHER
# ==========================================
# We need to encrypt a message by shifting every letter forward by 3.
# We will do this by converting the letter to its secret ASCII number, adding 3, 
# and converting it back!

message = "hacker"
encrypted_message = ""
shift_amount = 3

print("Original message:", message)

# TODO: Build the encryptor.
# 1. Create a for loop that goes through each 'letter' in the message.
# 2. Inside the loop, find the ASCII number of the letter using ord().
# 3. Add the shift_amount to that number.
# 4. Turn the new number back into a letter using chr().
# 5. Add the new letter to the encrypted_message.

# --- Write your loop below ---



# --- Do not change the code below ---
print("Encrypted message:", encrypted_message)

# BONUS QUESTION: What happens if you try to encrypt the letter 'z'? 
# Try changing the message to "zebra" and see what happens.
