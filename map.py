import pygame
import constants as c

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, _, _, _, 1, 1, 1, _, 1],
    [1, _, _, _, 1, _, 1, _, _, 1, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, 1, _, _, 1, _, 1],
    [1, _, 1, 1, _, 1, _, 1, _, _, _, _, _, 1, _, 1],
    [1, _, 1, _, _, 1, _, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        # generating the world map
        for y, row in enumerate(mini_map):
            for x, col in enumerate(row):
                if col:
                    self.world_map[(x, y)] = col

    def draw(self):
        [pygame.draw.rect(self.game.window, "darkgray", (pos[0] * 100, pos[1] * 100, 100, 100), 2)
            for pos in self.world_map]

