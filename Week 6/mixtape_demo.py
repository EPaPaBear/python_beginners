# ==========================================
# WEEK 5 PROJECT: MIXTAPE OS (Playlist Manager)
# ==========================================

# ------------------------------------------
# PHASE 1: The Queue
# ------------------------------------------
# TODO 1: Create an empty LIST called 'playlist'.
# This will hold all of our song titles in order.
playlist = []

# ------------------------------------------
# PHASE 2: The Functions (Tools)
# ------------------------------------------
def add_song():
    print("\n--- ADD A TRACK ---")
    # TODO 2: Ask the user for the name of the song.
    
    # TODO 3: Use the .append() method to add the song to the playlist list.
    
    print("Track added to queue!")

def show_queue():
    print("\n--- UP NEXT ---")
    # TODO 4: Check if the playlist is empty.
    # Use the len() function! IF len(playlist) is 0: print "The queue is empty."
    
    
    # TODO 5: ELSE, use a FOR loop to print every song in the playlist.
    
    
    print("---------------")

def play_next():
    print("\n--- NOW PLAYING ---")
    # TODO 6: Check if there are songs to play. IF len(playlist) > 0:
    # 1. Remove the first song using .pop(0) and store it in a variable called 'current_song'.
    # 2. Print a message saying "Now spinning: [current_song]"
    
    
    # TODO 7: ELSE: print "Nothing to play! Add some tracks."
    pass # Delete 'pass' when you write your code.


# ------------------------------------------
# PHASE 3: The Main System Loop
# ------------------------------------------
print("Booting MixTape OS...")

# TODO 8: Create a 'while True' loop for the menu.
# Inside the loop:
# 1. Print options: [1] Add Song  [2] View Queue  [3] Play Next  [4] Turn Off Player
# 2. Ask the user for their choice using input().
# 3. Use IF/ELIF to call the right function.
# 4. If they choose [4], use 'break' to stop the loop.