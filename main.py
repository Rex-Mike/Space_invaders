import pygame
from asset_pkg import ship
from asset_pkg import opponent_ships
from asset_pkg import bullet
from asset_pkg import dots
from random import randint
pygame.init()

# Screen Variables
size = [1000, 800]
background_color = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode(size)

bullet_position = None

bullets_event = pygame.USEREVENT + 1
# pygame.time.set_timer(bullets_event, 300)

running = True       
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_SPACE and bullet_position is None:
                ship_rect = ship.player_ship()
                bullet_position = list(ship_rect.midtop)
                pygame.time.set_timer(bullets_event, 500)
                
        if event.type == bullets_event:
            ship_rect = ship.player_ship()
            bullet_position = list(ship_rect.midtop)

    screen.fill(background_color)
    
    # For the dots
    dots.show_dot_on_screen(screen, size)
    
    # For the opponent Ship 
    """Below ///"""
    all_ships = opponent_ships.opponent(screen)

    # For the Player's Ship
    ship.player_move(screen,size)

    # Bullet
    bullet.shoot(screen, bullet_position, all_ships)
    
    # Update the display as in show the display to the user
    pygame.display.flip()

pygame.quit()