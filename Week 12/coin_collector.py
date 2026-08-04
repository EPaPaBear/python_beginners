# ==========================================
# WEEK 11 PROJECT: THE COIN COLLECTOR
# ==========================================
import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Coin Collector")
clock = pygame.time.Clock()

# --- Pre-loading a Font for the Score ---
# Pygame takes 3 steps to draw text. We setup the font here.
game_font = pygame.font.SysFont("Arial", 36, bold=True)

# --- Player Data ---
player_x = 400
player_y = 300
player_size = 50
player_speed = 7

# --- Coin Data ---
coin_size = 30
# Start the coin at a random location!
coin_x = random.randint(0, WIDTH - coin_size)
coin_y = random.randint(0, HEIGHT - coin_size)

# --- Game State ---
score = 0

running = True
while running:
    # 1. EVENT HANDLING (Quit button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # ----------------------------------------------------
    # 2. PLAYER MOVEMENT & BOUNDARIES (From Week 10)
    # ----------------------------------------------------
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:  player_x -= player_speed
    if keys[pygame.K_RIGHT]: player_x += player_speed
    if keys[pygame.K_UP]:    player_y -= player_speed
    if keys[pygame.K_DOWN]:  player_y += player_speed
    
    # Boundary Cage
    if player_x < 0: player_x = 0
    if player_x > WIDTH - player_size: player_x = WIDTH - player_size
    if player_y < 0: player_y = 0
    if player_y > HEIGHT - player_size: player_y = HEIGHT - player_size

    # ----------------------------------------------------
    # 3. BUILD THE RECTANGLES (Hitboxes)
    # ----------------------------------------------------
    # We must rebuild the invisible hitboxes every frame so they match 
    # the new X and Y coordinates!
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)
    
    # ----------------------------------------------------
    # 4. COLLISION DETECTION (The New Stuff!)
    # ----------------------------------------------------
    # TODO 1: Check if the player_rect overlaps with the coin_rect
    # Syntax hint: if player_rect.colliderect(coin_rect):
    
        
        # TODO 2: If they touch, add 1 to the 'score' variable
        
        
        # TODO 3: Teleport the coin to a new random X and Y coordinate!
        # Hint: coin_x = random.randint(0, WIDTH - coin_size)
        
        
    # ----------------------------------------------------
    # 5. DRAW THE FRAME
    # ----------------------------------------------------
    screen.fill((20, 20, 40)) # Dark blue background
    
    # Draw the Coin (Yellow)
    pygame.draw.rect(screen, (255, 215, 0), coin_rect)
    
    # Draw the Player (Cyan)
    pygame.draw.rect(screen, (0, 255, 255), player_rect) 
    
    # Draw the Score Text
    # (Text must be "Rendered" into an image, then "Blitted" onto the screen)
    score_text_image = game_font.render(f"SCORE: {score}", True, (255, 255, 255))
    screen.blit(score_text_image, (10, 10)) # Draw it at top-left (10, 10)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()