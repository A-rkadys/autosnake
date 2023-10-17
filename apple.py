from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    applepicture,
    MAX_X, MAX_Y,
    PLAYER_WIDTH, PLAYER_HEIGHT
)
from math import floor
from pygame import Surface, image
from pygame.sprite import Sprite
from random import randint

class Pomme(Sprite):

    def __init__(self):
        super(Pomme, self).__init__() 
        #self.surf = Surface((33, 28))
        #self.rect = self.surf.get_rect()
        self.image = image.load(applepicture)
        self.rect = self.image.get_rect()
        self.replace()

    def replace(self):
        self.rect.move_ip(
            PLAYER_WIDTH * (randint(0, MAX_X) - (self.rect.left / PLAYER_WIDTH)),
            PLAYER_WIDTH * (randint(0, MAX_Y) - (self.rect.top / PLAYER_HEIGHT))
        )
        print(f"x:{self.rect.left}\ny: {self.rect.top}\n")

