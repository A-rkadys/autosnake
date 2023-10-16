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
        self.surf = py.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


py.init()

#taille de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#creation de l'écran
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ADDENEMY = py.USEREVENT +1
py.time.set_timer(ADDENEMY, 250)

player = Player()



all_sprites = py.sprite.Group()
all_sprites.add(player)

clock = py.time.Clock()

#screen refresh
py.display.flip()

#boucle infinie
running2 = False
running = True
count = 60
while running:
    for event in py.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False


    pressed_keys = py.key.get_pressed()
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((0, 0, 0))
    #count += 0.1
    time += 1
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Update the display
    py.display.flip()
    clock.tick(count)

while running2:
    for event in py.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running2 = False
        elif event.type == QUIT:
            running2 = False
        
    screen_score.fill((0, 0, 0))
    screen_score.blit(text, textRect)
    screen_score.blit(text2, textRect2)

    py.display.update()
    py.display.flip()