import pygame
import constants as c
from player import *
from map import *

from sys import exit


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), vsync=1)
        self.clock = pygame.time.Clock()
        self.player = Player(300, 300)

    def update(self):
        self.player.update()
        self.clock.tick(60)
        pygame.display.set_caption(f"raycaster - fps {str(self.clock.get_fps())}")
        pygame.display.flip()

    def new_game(self):
        pass

    def draw(self):
        self.window.fill("black")

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
