import pygame
from random import randint
pygame.init()

number_of_dots = 5


def show_dot_on_screen(screen,size):
    for dot in range(number_of_dots):
        x = randint(0,size[0])
        y = randint(0, size[1])
        radius = randint(1,4)
        trans = randint(0, 255) 
        dia_of_circle_surface = radius*2
        circle_surface = pygame.Surface((dia_of_circle_surface, dia_of_circle_surface), pygame.SRCALPHA)
        rgba_dot_color = (255, 255, 255, trans)
        pygame.draw.circle(circle_surface, rgba_dot_color, [dia_of_circle_surface//2, dia_of_circle_surface//2], radius)
        screen.blit(circle_surface, (x, y))
