from enum import Enum
from pygame import Surface, Rect
from pygame.sprite import Sprite
from constants import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PLAYER_WIDTH, PLAYER_HEIGHT,
    MAX_X, MAX_Y,
    WHITE
)

WIDTH_LIMIT = MAX_X * PLAYER_WIDTH
HEIGHT_LIMIT = MAX_Y * PLAYER_HEIGHT

DIR_LEFT:int = 0
DIR_UP:int = 1
DIR_RIGHT:int = 2
DIR_DOWN:int = 3

def change_direction(dir:int, pressed_keys) -> int:
    new_dir = dir
    if (pressed_keys[K_LEFT] and (dir & 1)):
        new_dir = DIR_LEFT
    elif (pressed_keys[K_UP] and (dir & 1) == 0):
        new_dir = DIR_UP
    elif (pressed_keys[K_RIGHT] and (dir & 1)):
        new_dir = DIR_RIGHT
    elif (pressed_keys[K_DOWN] and (dir & 1) == 0):
        new_dir = DIR_DOWN
    return (new_dir)

class Player(Sprite):

    body:       list[Rect]
    direction:  int
    length:     int

    def __init__(self) -> None:
        super(Player, self).__init__()
        self.surf = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        sw = (SCREEN_WIDTH >> 1)
        sh = (SCREEN_HEIGHT >> 1)
        self.body = [self.rect]
        self.length = 1
        self.rect.move_ip(
            sw - (sw % PLAYER_WIDTH),
            sh - (sh % PLAYER_HEIGHT)
        )
        self.direction = DIR_LEFT

    def grow(self) -> None:
        self.body.append(self.body[self.length-1].copy())
        self.length += 1

    def update(self, pressed_keys) -> None:
        self.direction = change_direction(self.direction, pressed_keys)
        # To correct position if oob (horizontal axis)
        if (self.rect.left < PLAYER_WIDTH and self.direction == DIR_LEFT):
            return
        if (self.rect.top < PLAYER_HEIGHT and self.direction == DIR_UP):
            return
        if (self.rect.left >= WIDTH_LIMIT and self.direction == DIR_RIGHT):
            return
        if (self.rect.top >= HEIGHT_LIMIT and self.direction == DIR_DOWN):
            return
        i = self.length - 1
        while (i > 0):
            self.body[i].move_ip(
                self.body[i - 1].left - self.body[i].left,
                self.body[i - 1].top - self.body[i].top
            )
            i -= 1
        self.rect.move_ip(
            PLAYER_WIDTH * ((self.direction & 1) == 0) * ((self.direction % 4) - 1),
            PLAYER_HEIGHT * (self.direction & 1) * ((self.direction % 4) - 2)
        )

