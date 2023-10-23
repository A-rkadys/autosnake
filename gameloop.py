from random import randint
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    MUSICS,
    SCORE_INCREMENT,
    BLACK,
    FONT,
    BODY_SURFACE,
    CLOCK_TICK,
    QUIT, 
    K_ESCAPE,
    #OOF
)
import pygame as py
from player import Player
from apple import Pomme

def gameloop():
    screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py.display.flip()
    player = Player()
    apple = Pomme()
    all_sprites = py.sprite.Group()
    all_sprites.add(player)
    clock = py.time.Clock()
    running = True
    time = 0
    score = 0


    while running:
        if (not py.mixer.get_busy()):
            MUSICS[randint(0, MUSICS.__len__() - 1)].play()

        for event in py.event.get():
            if event.type == QUIT:
                running = False; break

        pressed_keys = py.key.get_pressed()
        if (pressed_keys[K_ESCAPE]):
            running = False; break
        
        player.update(pressed_keys)

        if player.rect.colliderect(apple.rect):
            score += SCORE_INCREMENT
            apple.replace()
            player.growth()
            #OOF.play()

        screen.fill(BLACK)
        screen.blit(apple.image, apple.rect)

        i = player.l_body - 1
        while (i):
        	screen.blit(BODY_SURFACE, player.body[i]); i -= 1
        screen.blit(player.surf, player.rect)

        score_text = FONT.render(f'Score: {score}', True, (0, 255, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(apple.image, apple.rect)

        # Update the display
        py.display.flip()
        clock.tick(CLOCK_TICK)

