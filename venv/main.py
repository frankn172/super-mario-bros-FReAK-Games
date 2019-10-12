import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Insert Title Here")

    while True:
        screen.fill((255, 255, 255))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


run_game()
