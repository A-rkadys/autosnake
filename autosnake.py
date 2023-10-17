import pygame as py
import random as r
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    KEYDOWN, K_ESCAPE,
    QUIT
)
from player import Player, Sprite

py.init()

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
time = 0
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

