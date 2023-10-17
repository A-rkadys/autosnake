from constants import SCREEN_WIDTH, SCREEN_HEIGHT, applepicture
from math import floor
from pygame import Surface, image
from pygame.sprite import Sprite
from random import randint

class Pomme(Sprite):

    DIM_X:int = 33
    DIM_Y:int = 28
    MAX_X:int = floor(SCREEN_WIDTH / DIM_X) - 1
    MAX_Y:int = floor(SCREEN_HEIGHT / DIM_Y) - 1

    def __init__(self):
        super(Pomme, self).__init__() 
        #self.surf = Surface((33, 28))
        #self.rect = self.surf.get_rect()
        self.image = image.load(applepicture)
        self.rect = self.image.get_rect()
        self.replace()

    def replace(self):
        self.rect.move_ip(
            self.DIM_X * (randint(0, self.MAX_X) - (self.rect.left / self.DIM_X)),
            self.DIM_Y * (randint(0, self.MAX_Y) - (self.rect.top / self.DIM_Y))
        )
        print(f"x:{self.rect.left}\ny: {self.rect.top}\n")

