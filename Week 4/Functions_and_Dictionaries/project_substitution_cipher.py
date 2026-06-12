# ==========================================
# WEEK 4 PROJECT: THE ENCRYPTION ENGINE
# ==========================================
# Last week, we used ASCII math to shift letters. That is easy to crack.
# Today, we are using a Dictionary to create a Substitution Cipher, 
# mapping every letter to a completely random symbol or letter.

# This is our Encryption Key:
cipher_key = {
    "a": "q", "b": "w", "c": "e", "d": "r", "e": "t",
    "f": "y", "g": "u", "h": "i", "i": "o", "j": "p",
    "k": "a", "l": "s", "m": "d", "n": "f", "o": "g",
    "p": "h", "q": "j", "r": "k", "s": "l", "t": "z",
    "u": "x", "v": "c", "w": "v", "x": "b", "y": "n", "z": "m",
    " ": " " # Keep spaces as spaces
}

# TODO: Build the Encryptor
# 1. Define a function called 'encrypt_message' that takes 'message' as an argument.
# 2. Create an empty string variable called 'encrypted_text'.
# 3. Use a FOR loop to go through each 'letter' in the message.
# 4. Look up that letter in the 'cipher_key' dictionary to get the new symbol.
# 5. Add the new symbol to 'encrypted_text'.
# 6. RETURN the 'encrypted_text'.

# --- Write your function below ---



# --- Run the Engine ---
print("--- SUBSTITUTION ENGINE ---")
user_message = input("Enter a message to encrypt (lowercase only): ")

# Call your function here and print the result!
# final_message = encrypt_message(user_message)
# print("Encrypted:", final_message)