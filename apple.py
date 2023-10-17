from pygame import Surface, image
import random as r
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, applepicture
from pygame.sprite import Sprite


class Pomme(Sprite):
    def __init__(self):
        super(Pomme, self).__init__() 
        self.surf = Surface((33, 28))
        self.image = image.load(applepicture)
        self.rect = self.surf.get_rect()
        self.rect = self.image.get_rect()
    def replace(self):
            self.rect.move_ip(r.randint(0, SCREEN_WIDTH) - self.rect.right, 
            r.randint(0, SCREEN_HEIGHT) - self.rect.bottom)