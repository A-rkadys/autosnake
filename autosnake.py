import pygame as py
import sys as sys
import os as os
from constants import *
from player import Player
from apple import Pomme


time = 0
score = 0

py.init()
py.font.init()



#creation de l'écran
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ADDENEMY = py.USEREVENT +1
py.time.set_timer(ADDENEMY, 250)

player = Player()
pomme = Pomme()


all_sprites = py.sprite.Group()
all_sprites.add(player)

clock = py.time.Clock()

#screen refresh
py.display.flip()

#boucle infinie
running2 = False
running = True
font = py.font.Font(None, 36)
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
    time += 1
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        py.draw.rect(screen, (255   , 0, 0), pomme)

    score_text = font.render(f'Score: {score}', True, (0, 255, 0))
    screen.blit(score_text, (10, 10))
    
    # Update the display
    py.display.flip()
    clock.tick(count)
    if player.rect.colliderect(pomme.rect):
        score += score_increment
        pomme.replace()

    """if player.rect.colliderect(,):
        player.kill()"""

    

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