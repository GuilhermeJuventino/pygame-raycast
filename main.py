import pygame
import constants as c
from player import *
from map import *
from raycasting import *
from object_renderer import *

from sys import exit


class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), vsync=1)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.delta_time = self.clock.tick(c.FPS)
        pygame.display.set_caption(f"raycaster - fps {self.clock.get_fps() :.1f}")
        pygame.display.flip()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def draw(self):
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()

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

