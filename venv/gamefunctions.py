import sys
from time import sleep
import pygame


def check_keydown_events(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True


def check_keyup_events(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False


def check_events(mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)


def draw_screen(screen, mario):
    screen.fill((255, 255, 255))
    mario.blitme()
    sleep(0.005)
    pygame.display.flip()
