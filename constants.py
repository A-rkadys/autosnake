from pygame import mixer
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    K_ESCAPE,
    QUIT
)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)

#taille de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25
SCREEN_WIDTH -= SCREEN_WIDTH % PLAYER_WIDTH
SCREEN_HEIGHT -= SCREEN_HEIGHT % PLAYER_HEIGHT
MAX_X:int = int(SCREEN_WIDTH / PLAYER_WIDTH)
MAX_Y:int = int(SCREEN_HEIGHT / PLAYER_HEIGHT)

score_increment = 1

applepicture = "Pomme.png"


mixer.init(44100, 32, 2)
PIPI = mixer.Sound(file = "pipi.wav")

#60000000000000000000
CLOCK_TICK = 5
