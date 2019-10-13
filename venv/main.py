import pygame
from player import Mario
import gamefunctions as gf


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Insert Title Here")
    mario = Mario(screen)

    while True:
        gf.check_events(mario)
        mario.update()
        gf.draw_screen(screen, mario)


run_game()
