import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

tank = pygame.image.load('tank_movements_events/tank.png').convert_alpha()

tank_get_rect = tank.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        print(event)

    pygame.display.update()

    tank_get_rect.center = pygame.mouse.get_pos()

    screen.fill((255, 255, 255))
    screen.blit(tank, tank_get_rect.topleft)

    pygame.display.update()
