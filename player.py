import pygame
import constants as c


class Player:
    def __init__(self, x, y):
        self.color = pygame.Color("yellow")
        self.point_size = 8
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.point_size, self.point_size))

    def input(self):
        self.keystate = pygame.key.get_pressed()

        if self.keystate[pygame.K_a]:
            self.x -= 5
        if self.keystate[pygame.K_d]:
            self.x += 5
        if self.keystate[pygame.K_w]:
            self.y -= 5
        if self.keystate[pygame.K_s]:
            self.y += 5

    def update(self):
        self.input()
