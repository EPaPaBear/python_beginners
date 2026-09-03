# ==========================================
# EXERCISE 2: THE ARCHITECT (REFACTORING)
# ==========================================
# The Problem: This code works perfectly. It prints a store receipt.
# But it is terribly written. It violates the D.R.Y. rule (Don't Repeat Yourself).
# If the store had 1,000 items, this code would be 4,000 lines long!
#
# YOUR MISSION:
# Make it elegant. Replace the manual printing with a List, a Dictionary, 
# and a single 'for' loop.

print("--- OLD, UGLY RECEIPT ---")
print("Item: Apple - $2")
print("Item: Bread - $4")
print("Item: Milk - $3")
print("Item: Eggs - $5")
print("Item: Cheese - $6")

total = 2 + 4 + 3 + 5 + 6
print(f"Total: ${total}")


print("\n--- NEW, ELEGANT RECEIPT ---")
# TODO 1: Create a dictionary holding the items and their prices.
# cart = { ... }


# TODO 2: Create a variable to track the new total.
# new_total = 0


# TODO 3: Write a FOR loop to go through the dictionary.
# Print each item and its price, and add the price to new_total.


# TODO 4: Print the final new_total. It should match the ugly code!