import sys
import pygame
from time import sleep
from player import Mario


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Insert Title Here")
    mario = Mario(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    mario.moving_right = True
                elif event.key == pygame.K_LEFT:
                    mario.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    mario.moving_right = False
                elif event.key == pygame.K_LEFT:
                    mario.moving_left = False

        screen.fill((255, 255, 255))
        mario.update()
        mario.blitme()
        sleep(0.001)
        pygame.display.flip()


run_game()
