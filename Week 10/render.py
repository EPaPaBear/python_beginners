# ==========================================
# WEEK 9 PROJECT: THE RENDER LOOP
# ==========================================
import pygame

# --- PYGAME SETUP (Do not change this) ---
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Canvas")
clock = pygame.time.Clock() # This controls our Frame Rate (FPS)
# -----------------------------------------

# ------------------------------------------
# PHASE 1: Data & Variables
# ------------------------------------------
# TODO 1: Create variables for our Player's position.
# Create 'player_x' and set it to 400 (the middle of the screen)
# Create 'player_y' and set it to 300


# TODO 2: Create RGB color variables (Tuples)
# Example: RED = (255, 0, 0)
# Create a color for the BACKGROUND (e.g. Black -> 0, 0, 0)
# Create a color for the PLAYER (e.g. Green -> 0, 255, 0)



# ------------------------------------------
# PHASE 2: The Game Loop
# ------------------------------------------
running = True

print("Engine starting. Look at the new window!")

while running:
    # 1. Event Handling (Checking if the user clicked the 'X' to close the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # ----------------------------------------------------
    # 2. CLEAR THE SCREEN (Erase the old frame)
    # ----------------------------------------------------
    # TODO 3: Use screen.fill() and pass in your BACKGROUND color variable.
    
    
    # ----------------------------------------------------
    # 3. UPDATE THE DATA (Move the player)
    # ----------------------------------------------------
    # TODO 4: Add 5 to player_x so it moves to the right!
    
    
    # ----------------------------------------------------
    # 4. DRAW THE NEW FRAME
    # ----------------------------------------------------
    # We create a rectangle using: pygame.Rect(x, y, width, height)
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    
    # TODO 5: Tell pygame to draw it!
    # Syntax: pygame.draw.rect(screen, YOUR_COLOR_VARIABLE, player_rect)
    
    
    
    # ----------------------------------------------------
    # 5. SHOW IT TO THE HUMAN (Flip the display)
    # ----------------------------------------------------
    # TODO 6: Update the screen so we can see the changes.
    # Syntax: pygame.display.flip()
    
    
    
    # Lock the game to 60 Frames Per Second
    clock.tick(60)

# Once the while loop breaks, quit pygame safely.
pygame.quit()