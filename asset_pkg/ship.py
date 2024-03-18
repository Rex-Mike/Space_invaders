import pygame
pygame.init()

position = [500,650]
ship_width, ship_height  = 150, 150

ship = pygame.image.load("pictures/player_ship.webp") #.convert_alpha()
scaled_ship = pygame.transform.scale(ship, (ship_width, ship_height))



def player_ship():
    ship_rect = scaled_ship.get_rect()
    ship_rect.topleft= position
    return  ship_rect


def player_move(screen, size):
    ship_rect = player_ship()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        position[1] = max (position[1] - 1, 0)
    elif keys[pygame.K_DOWN]:
        position[1] = min (position[1] + 1, size[1] - 150)
    elif keys[pygame.K_LEFT]:
        position[0] = max(position[0] - 1, 0)
    elif keys[pygame.K_RIGHT]:
        position[0] = min(position[0] + 1, size[0] - 150)
    
    ship_rect.topleft= position

    screen.blit(scaled_ship, ship_rect)





