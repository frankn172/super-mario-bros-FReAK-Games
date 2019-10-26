import pygame
from player import Mario
from goomba import Goomba
import gamefunctions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Insert Title Here")
    mario = Mario(screen)
    enemies = Group()
    enemies.add(Goomba(screen))

    while True:
        gf.check_events(mario, enemies)
        mario.update()
        gf.draw_screen(screen, mario, enemies)


run_game()
