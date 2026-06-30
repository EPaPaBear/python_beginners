# ==========================================
# WEEK 5 PROJECT: THE SECURE COMM-LINK
# ==========================================

# ------------------------------------------
# PHASE 1: The Database
# ------------------------------------------
# TODO 1: Create an empty dictionary called 'directory'
# This will store the Name (Key) and the Phone Number (Value).
directory = {}

# ------------------------------------------
# PHASE 2: The Functions (Tools)
# ------------------------------------------
def add_contact():
    print("\n--- ADD NEW CONTACT ---")
    # TODO 2: Ask the user for a name using input()
    
    # TODO 3: Ask the user for a phone number using input()
    
    # TODO 4: Save it to the dictionary!
    # Syntax hint: dictionary_name[key] = value
    
    print("Contact saved successfully.")

def search_contact():
    print("\n--- SEARCH DIRECTORY ---")
    # TODO 5: Ask the user for the name they want to find.
    
    
    # TODO 6: Check if the name exists in the directory.
    # Use an IF statement with the 'in' keyword!
    # IF the name is in the directory:
    #     Print the name and the phone number.
    # ELSE:
    #     Print an error saying the contact was not found.
    pass # Delete this 'pass' when you write your code.

def show_all():
    print("\n--- ACTIVE DIRECTORY ---")
    # TODO 7: Use a FOR loop to print every contact.
    # Hint: for name, number in directory.items():
    
    print("------------------------")

# ------------------------------------------
# PHASE 3: The Main System Loop
# ------------------------------------------
print("Booting Comm-Link OS...")

# TODO 8: Create a 'while True' loop to keep the program running forever.
# Inside the loop:
# 1. Print the menu options: [1] Add  [2] Search  [3] Show All  [4] Quit
# 2. Ask the user for their choice.
# 3. Use an IF/ELIF block to call the correct function based on their choice.
# 4. If they pick [4], 'break' the loop to shut down the program.