from pygame import Surface
import random as r
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.sprite import Sprite


class Pomme(Sprite):
    def __init__(self):
        super(Pomme, self).__init__()
        self.surf = Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    def replace(self):
            self.rect.move_ip(r.randint(0, SCREEN_WIDTH) - self.rect.right, 
            r.randint(0, SCREEN_HEIGHT) - self.rect.bottom)