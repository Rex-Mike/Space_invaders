import pygame
pygame.init()
from . import bullet

all_ships = [] # Image, rectangle surface

positions = [[70, 100], [170,100], [270,100], [370, 100], [470, 100], [570,100], [670,100], [770, 100], [870, 100],
             [70, 20], [170,20], [270,20], [370, 20], [470, 20], [570,20], [670,20], [770, 20], [870, 20],
             [70, 180], [170,180], [270,180], [370, 180], [470, 180], [570,180], [670,180], [770, 180], [870, 180]]

directions = []
right_max_positions = [position[:] for position in positions]
left_max_positions = [position[:] for position in positions]


for position in right_max_positions:
    position[0] += 70
for position in left_max_positions:
    position[0] -= 60

for _ in positions:
    opponent_ship = pygame.image.load("./pictures/opponent_ship.png")
    
    opponent_width, opponent_height = 60, 60
    opponent_ship_scaled = pygame.transform.scale(opponent_ship, [opponent_width, opponent_height])

    opponent_ship_rect = opponent_ship_scaled.get_rect()
    
    ship = [opponent_ship_scaled, opponent_ship_rect]
    all_ships.append(ship)
    directions.append(0.2)

def opponent(screen):
    ships_to_remove = []
    for i, (ship, position, right_max_position, left_max_position) in enumerate(zip (all_ships, positions, right_max_positions, left_max_positions)): # (0, (ship1, position [100, 200], maxposition))
        ship[1].topleft = position
        # For the ships to move to the left end then move to the right then go up again
        position[0] += directions[i]

        if position[0] <= left_max_position[0] or position[0] >= right_max_position[0]:
            position[1] += 5
            directions[i] *= -1

        if position[1] >= 800:
            ships_to_remove.append(ship)
        
        
        screen.blit(ship[0], ship[1])

    #  FOR DEBUGGING........................................
    for ship in all_ships:
        # Draw the ship
        screen.blit(ship[0], ship[1].topleft)
        # Draw a rectangle around the ship for debugging
        pygame.draw.rect(screen, (255, 0, 0), ship[1], 2)

    
    return (all_ships)
    




