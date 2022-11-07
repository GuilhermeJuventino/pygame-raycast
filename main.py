import pygame
import constants as c
from player import *

from sys import exit

pygame.init()

window = pygame.display.set_mode(c.SCREEN_SIZE, vsync=1)
clock = pygame.time.Clock()

player = Player(300, 300)

while True:
    clock.tick(60)
    window.fill(pygame.Color("darkgrey"))

    player.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.update()
    pygame.display.flip()

