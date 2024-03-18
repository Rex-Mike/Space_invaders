import pygame
pygame.init()
from . import ship


  
bullet  = pygame.image.load("pictures/bullet.png")
bullet_width, bullet_height = 40, 40
bullet_scaled = pygame.transform.scale(bullet, (bullet_width, bullet_height))


def shoot(screen, bullet_position, all_ships):
    if bullet_position is None:
        return None

    bullet_position[1] -= 2
    bullet_rect = bullet_scaled.get_rect()
    bullet_rect.center = bullet_position

    if bullet_position[1] < 0:
        return None

    screen.blit(bullet_scaled, bullet_rect)

    ships_to_remove = []
    for ship in all_ships:
        if bullet_rect.colliderect(ship[1]):  # Assuming ship[1] is the ship's rect
            ships_to_remove.append(ship)

    for ship in ships_to_remove:
        all_ships.remove(ship)
    
    # If any ship was hit, return None to indicate the bullet should disappear.
    # Otherwise, return the bullet's updated position.
    return None if ships_to_remove else bullet_position




