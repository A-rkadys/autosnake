from pygame import Surface
from pygame.sprite import Sprite
from constants import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PLAYER_WIDTH, PLAYER_HEIGHT,
    MAX_X, MAX_Y,
    WHITE
)

class Player(Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(
            SCREEN_WIDTH - ((SCREEN_WIDTH >> 1) % PLAYER_WIDTH),
            SCREEN_HEIGHT - ((SCREEN_HEIGHT >> 1) % PLAYER_HEIGHT)
        )

    def update(self, pressed_keys):
        self.rect.move_ip(
            PLAYER_WIDTH * (pressed_keys[K_RIGHT] - pressed_keys[K_LEFT]),
            PLAYER_HEIGHT * (pressed_keys[K_DOWN] - pressed_keys[K_UP])
        )
        # To correct position if oob (horizontal axis)
        self.rect.left *= (0 < self.rect.left and self.rect.left < SCREEN_WIDTH)
        self.rect.left += SCREEN_WIDTH * (self.rect.left > SCREEN_WIDTH)
        self.rect.right = self.rect.left + PLAYER_WIDTH
        # To correct position if oob (vertical axis)
        self.rect.top *= (0 < self.rect.top and self.rect.top < SCREEN_HEIGHT)
        self.rect.top += SCREEN_HEIGHT * (self.rect.top > SCREEN_HEIGHT)
        self.rect.bottom = self.rect.top + PLAYER_HEIGHT

