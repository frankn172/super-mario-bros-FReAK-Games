import pygame
from player import Mario
from goomba import Goomba
from backgroud import Background
import gamefunctions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Insert Title Here")
    mario = Mario(screen)
    enemies = Group()
    enemies.add(Goomba(screen))
    background = Background(screen)
    background.setTiles([["images/1-1/tile000.png",
                          "images/1-1/tile001.png",
                          "images/1-1/tile002.png",
                          "images/1-1/tile003.png",
                          "images/1-1/tile004.png",
                          "images/1-1/tile005.png",
                          "images/1-1/tile006.png",
                          "images/1-1/tile007.png",
                          "images/1-1/tile008.png",
                          "images/1-1/tile009.png",
                          "images/1-1/tile010.png",
                          "images/1-1/tile011.png",
                          "images/1-1/tile012.png",
                          "images/1-1/tile013.png",
                          "images/1-1/tile014.png",
                          "images/1-1/tile015.png",
                          "images/1-1/tile015.png"]])
    background.scroll(0, 0)

    while True:
        gf.check_events(mario, enemies)
        mario.update()
        gf.draw_screen(screen, mario, enemies, background)


run_game()
