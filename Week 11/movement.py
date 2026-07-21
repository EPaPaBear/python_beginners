# ==========================================
# WEEK 10 PROJECT: THE CONTROLLER & THE CAGE
# ==========================================
# If Pygame 3.14.x is missing wheels, use: pip install pygame-ce
import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player Movement & Boundaries")
clock = pygame.time.Clock()

# --- Player Data ---
player_x = 400
player_y = 300
player_size = 50
player_speed = 5  # How fast the player moves per frame

running = True
while running:
    # 1. Check for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # ----------------------------------------------------
    # 2. GET PLAYER INPUT (Polling the keyboard)
    # ----------------------------------------------------
    # This gets a list of every key on the keyboard and whether it is being pressed True/False
    keys = pygame.key.get_pressed()
    
    # TODO 1: Move Right
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
        
    # TODO 2: Move Left (Subtract from player_x)
    
    
    # TODO 3: Move Up (Remember, Y goes DOWN in computers! To go up, subtract!)
    
    
    # TODO 4: Move Down (Add to player_y)
    
    
    
    # ----------------------------------------------------
    # 3. BOUNDARY DETECTION (The Invisible Cage)
    # ----------------------------------------------------
    # Left Wall
    if player_x < 0:
        player_x = 0  # Push them back to 0
        
    # Right Wall
    # TODO 5: If player_x is greater than (WIDTH - player_size), push them back to (WIDTH - player_size)
    
    
    # Top Wall
    # TODO 6: If player_y is less than 0, push them back to 0.
    
    
    # Bottom Wall
    # TODO 7: If player_y is greater than (HEIGHT - player_size), push them back to (HEIGHT - player_size)
    
    
    
    # ----------------------------------------------------
    # 4. DRAW THE FRAME
    # ----------------------------------------------------
    screen.fill((30, 30, 40)) # Dark gray background
    
    # Build the player rectangle using our updated X and Y variables
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, (0, 255, 100), player_rect) # Draw in Green
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()