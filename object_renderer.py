import pygame
import constants as c


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.window = self.game.window
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture("resources/textures/sky.png", (c.SCREEN_WIDTH, c.HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_backgrounds()
        self.render_game_objects()

    def draw_backgrounds(self):
        self.sky_offset = (self.sky_offset + 4.0 * self.game.player.rel) % c.SCREEN_WIDTH

        # background (with scrolling)
        self.window.blit(self.sky_image, (-self.sky_offset, 0))
        self.window.blit(self.sky_image, (-self.sky_offset + c.SCREEN_WIDTH, 0))

        # floor
        pygame.draw.rect(self.window, c.FLOOR_COLOR, (0, c.HALF_HEIGHT, c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.window.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(c.TEXTURE_SIZE, c.TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture("resources/textures/1.png", ),
            2: self.get_texture("resources/textures/2.png", ),
            3: self.get_texture("resources/textures/3.png", ),
            4: self.get_texture("resources/textures/4.png", ),
            5: self.get_texture("resources/textures/5.png", ),
        }
