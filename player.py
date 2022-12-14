import pygame
import math
import constants as c

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = c.PLAYER_POS
        self.angle = c.PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = c.PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin

        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        if keys[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos

        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos

        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)

        self.check_wall_collision(dx, dy)

        self.angle %= math.tau


    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = c.PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        #pygame.draw.line(self.game.window, "yellow", (self.x * 100, self.y * 100),
         #                (self.x * 100 + c.SCREEN_WIDTH * math.cos(self.angle),
         #                 self.y * 100 + c.SCREEN_WIDTH * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.window, "green", (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pygame.mouse.get_pos()

        if mx < c.MOUSE_BORDER_LEFT or mx > c.MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos([c.HALF_WIDTH, c.HALF_HEIGHT])

        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max(-c.MOUSE_MAX_REL, min(c.MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * c.MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
