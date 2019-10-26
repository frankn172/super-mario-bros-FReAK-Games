import pygame
from pygame.sprite import Sprite


class PirahnaPlant(Sprite):
    def __init__(self, screen):
        super(PirahnaPlant, self).__init__()
        self.screen = screen

        # Load image
        self.image = pygame.image.load('images/goomba.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value of Koopa's position
        self.center = float(self.rect.centerx)

        # Set Movement Flags
        self.moving_up = False
        self.moving_down = True
        self.in_pipe = True

        # Timer, determines how long the plant is out of the pipe
        # TODO set variables for pipe location
        # TODO if mario is next to pipe, pirahna plant will not ascend

    def update(self):
        """Update Koopa position"""
        if self.moving_up:
            self.rect.centerx += 1
        if self.moving_down:
            self.rect.centerx -= 1
        # TODO Check if Koopa is Red, if so check if title is empty, if so fall down

    def blitme(self):
        """Draw Koopaa to the screen"""
        self.screen.blit(self.image, self.rect)
        pass
