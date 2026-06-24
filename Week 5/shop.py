# ==========================================
# PRACTICE: THE ITEM SHOP
# ==========================================

# TODO 1: Build the shop's inventory.
# Create a dictionary called 'shop_inventory'. 
# Give it 3 items (Keys) and assign them integer prices (Values).
# Example -> "Health Potion": 20


# The Player's Stats
player_gold = 100
player_items = [] # An empty list to hold the things they buy!

def show_items():
    print("\n--- WELCOME TO THE SHOP ---")
    # TODO 2: Write a FOR loop to display the shop's items.
    # Loop through the shop_inventory dictionary.
    # Print out the Item Name and its Price.
    pass # Remove 'pass' when you write your code

def buy_item(requested_item):
    # We need to tell the function to use the GLOBAL player variables
    global player_gold
    
    # TODO 3: Check if the item exists in the shop.
    # Use an IF statement with the 'in' keyword to check the dictionary.
    
    # TODO 4: If it exists, check if the player has enough gold.
    # To get the price, look it up in the dictionary: shop_inventory[requested_item]
    
    # TODO 5: If they have enough gold:
    # 1. Subtract the price from player_gold
    # 2. Use .append() to add the requested_item to the player_items list
    # 3. Print a success message!
    
    pass # Remove 'pass' when you write your code

# --- THE MAIN LOOP ---
# TODO 6: Build the store loop.
# Create a 'while True' loop.
# Inside the loop:
# 1. Show the user their current gold and their current player_items list.
# 2. Call the show_items() function so they can see what is for sale.
# 3. Ask them what they want to buy using input().
# 4. If they type "quit", break the loop.
# 5. Otherwise, pass their input into the buy_item() function!