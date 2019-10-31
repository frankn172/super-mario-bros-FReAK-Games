import pygame
from pygame.sprite import Group

import gamefunctions as gf
from backgroud import Background
from enemies import *
from player import Mario
from powerup import *


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((448, 224))
    pygame.display.set_caption("Super Mario Bros")
    mario = Mario(screen)
    enemies = Group()
    enemies.add(Goomba(y=c.GROUND_HEIGHT, x=150, direction=c.LEFT))
    powerups = Group()

    enemies.add(Goomba(y=c.GROUND_HEIGHT, x=150, direction=c.LEFT))
    enemies.add(Koopa(y=c.GROUND_HEIGHT, x=170))
    enemies.add(Goomba(y=c.GROUND_HEIGHT, x=190, direction=c.LEFT))
    enemies.add(Goomba(y=c.GROUND_HEIGHT, x=210, direction=c.LEFT))
    enemies.add(Goomba(y=c.GROUND_HEIGHT, x=240, direction=c.LEFT))
    enemies.add(Koopa(y=280, x=200, winged=True))
    enemies.add(PirahnaPlant(y=280, x=100))
    enemies.add(CheepCheep(y=50, x=100))
    enemies.add(Podaboo(x=200))
    enemies.add(FireBar(x=150, y=150))
    enemies.add(Blooper(x=200, y=100, mario=mario))
    enemies.add(FireBar(x=150, y=150))
    enemies.add(FireBar(x=150, y=150, radius=20))
    enemies.add(FireBar(x=150, y=150, radius=30))
    enemies.add(FireBar(x=150, y=150, radius=40))
    enemies.add(FireBar(x=150, y=150, radius=50))
    enemies.add(FireBar(x=150, y=150, radius=60))
    enemies.add(FireBar(x=150, y=150, radius=70))
    enemies.add(Blooper(x=200, y=100, mario=mario))

    powerups.add(Mushroom(x=20))
    powerups.add(Flower(x=250))
    powerups.add(Life(x=50))
    powerups.add(Star(x=10))

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
        gf.check_events(mario)
        mario.update()
        gf.update_enemies(mario, enemies, powerups)
        gf.draw_screen(screen, mario, enemies, powerups, background)


run_game()
