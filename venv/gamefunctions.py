import pygame
import sys
import os
import constants as c
from time import sleep


def check_keydown_events(event, mario):
    if event.key == pygame.K_RIGHT:
        mario.moving_right = True
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True
    if event.key == pygame.K_SPACE:
        if not mario.jumping and not mario.falling:
            mario.jumping = True
            mario.reset_jump_timer()


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


def update_enemies(mario, enemies, powerups):
    check_mario_enemy_collisions(mario, enemies)

    for enemy in enemies:
        enemy.update()

    for powerup in powerups:
        powerup.update()


def check_mario_enemy_collisions(mario, enemies):
    for enemy in enemies:
        # Checks if Mario stomped on an enemy
        if enemy.rect.left <= mario.rect.right <= enemy.rect.right or enemy.rect.left <= mario.rect.left <= enemy.rect.right:
            # TODO implement Mario death sequence
            if enemy.rect.top - 1 <= mario.rect.bottom <= enemy.rect.top + 1:
                enemy.state = c.JUMPED_ON
                return
            print('HI')


def draw_screen(screen, mario, enemies, powerups, background):
    screen.fill(background.color)
    if mario.moving_right:
        background.scroll(-20, 0)
    screen.blit(background.surface, [0, 0])
    mario.blitme(screen)
    for enemy in enemies:
            enemy.draw(screen)
    mario.blitme(screen)
    enemies.draw(screen)
    powerups.draw(screen)
    sleep(0.01)
    #pygame.display.flip()
    pygame.display.update()


def loadImage(fileName):
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + fileName + " - Check filename and path?")


def parseColor(color):
    if type(color) == str:
        # check to see if valid colour
        return pygame.Color(color)
    else:
        colourRGB = pygame.Color("white")
        colourRGB.r = color[0]
        colourRGB.g = color[1]
        colourRGB.b = color[2]
        return colourRGB
