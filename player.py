from pygame import Surface
from pygame.sprite import Sprite
from constants import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    SCREEN_WIDTH, SCREEN_HEIGHT,
    WHITE
)

class Player(Sprite):

    DIM_X = 25
    DIM_Y = 25
    MAX_X = SCREEN_WIDTH - DIM_X
    MAX_Y = SCREEN_HEIGHT - DIM_Y

    def __init__(self):
        super(Player, self).__init__()
        self.surf = Surface((self.DIM_X, self.DIM_Y))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.MAX_X >> 1, self.MAX_Y >> 1)

    def update(self, pressed_keys):
        self.rect.move_ip(
            self.DIM_X * (pressed_keys[K_RIGHT] - pressed_keys[K_LEFT]),
            self.DIM_Y * (pressed_keys[K_DOWN] - pressed_keys[K_UP])
        )
        # To correct position if oob (horizontal axis)
        self.rect.left *= (0 < self.rect.left and self.rect.left <= self.MAX_X)
        self.rect.left += self.MAX_X * (self.rect.left > self.MAX_X)
        self.rect.right = self.rect.left + self.DIM_X
        # To correct position if oob (vertical axis)
        self.rect.top *= (0 < self.rect.top and self.rect.top <= self.MAX_Y)
        self.rect.top += (self.MAX_Y) * (self.rect.top > self.MAX_Y)
        self.rect.bottom = self.rect.top + self.DIM_Y

