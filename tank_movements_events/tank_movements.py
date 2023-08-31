import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

tank = pygame.image.load('tank_movements_events/tank.png').convert_alpha()

x, y = 0, 0
move_x, move_y = 0, 0
tank_speed = 3

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x -= tank_speed + 5
            elif event.key == K_RIGHT:
                move_x += tank_speed + 5
            elif event.key == K_UP:
                move_y -= tank_speed + 5
            elif event.key == K_DOWN:
                move_y = tank_speed + 5
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                move_x = 0
            if event.key == K_UP or event.key == K_DOWN:
                move_y = 0

        x += move_x
        y += move_y

        screen.fill((255,255,255))
        screen.blit(tank,(x,y))

        pygame.display.update()
