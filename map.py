import pygame
import constants as c

def draw_map_2d(surface):
    level_map = []

    for row_index, row in enumerate(c.WORLD_LAYOUT):
        for col_index, col in enumerate(row):
            if c.WORLD_LAYOUT[row_index][col_index] == 1:
                #print("Wall")
                color = pygame.Color(1, 1, 1)
            else:
                #print("Empty")
                color = pygame.Color(0, 0, 0)
            x = col_index * 5
            y = row_index * 5
            new_rect = pygame.Rect(x, y, 5, 5)
            pygame.draw.rect(surface, color, new_rect)
