import pygame as py
from constants import *
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
	FONT = py.font.Font(None, 36)
	running = True
	time = 0
	score = 0
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

	    score_text = FONT.render(f'Score: {score}', True, (0, 255, 0))
	    screen.blit(score_text, (10, 10))
	    screen.blit(apple.image, apple.rect)
	    # Update the display
	    py.display.flip()
	    clock.tick(10)
	    if player.rect.colliderect(apple.rect):
	        score += score_increment
	        apple.replace()
