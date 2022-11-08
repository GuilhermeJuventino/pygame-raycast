import pygame
import constants as c


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.window = self.game.window
        self.wall_textures = self.load_wall_textures()
        self.sky_textures = self.get_texture("resources/textures/sky.png", (c.SCREEN_WIDTH, c.HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.render_game_objects()

    def draw_backgrounds(self):
        pass

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
