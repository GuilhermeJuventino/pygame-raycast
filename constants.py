import math

# game settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
FPS = 0

# player settings
PLAYER_POS = 1.5, 5 # mini-map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

# raycasting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = SCREEN_WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20
