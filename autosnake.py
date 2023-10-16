#snake

import pygame as py
import random as r
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

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
time = 0

#snake
class Player(py.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surf = py.Suface((25, 25))
