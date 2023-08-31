import pygame
from pygame.locals import *
from sys import exit
import math

pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

tank = pygame.image.load('tank/tanque.jpg').convert_alpha()
tank = pygame.transform.scale(tank, (303, 114))

# tank_get_rect = tank.get_rect()
tank_rotation_speed = 3
tank_speed = 3

x, y = SCREEN_SIZE[0] // 2 - 180, SCREEN_SIZE[1] // 2 
tank_angle = 180

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        tank_angle += tank_rotation_speed
    if keys[K_RIGHT]:
        tank_angle -= tank_rotation_speed
    if keys[K_UP]:
        x -= tank_speed * math.cos(math.radians(tank_angle))
        y += tank_speed * math.sin(math.radians(tank_angle))
    if keys[K_DOWN]:
        x += tank_speed * math.cos(math.radians(tank_angle))
        y -= tank_speed * math.sin(math.radians(tank_angle))

    rotated_tank = pygame.transform.rotate(tank, tank_angle)
    rotated_rect = rotated_tank.get_rect(center=(x, y))

    screen.fill((255, 255, 255))
    screen.blit(rotated_tank, rotated_rect.topleft)

    pygame.display.update()
    clock.tick(60)
