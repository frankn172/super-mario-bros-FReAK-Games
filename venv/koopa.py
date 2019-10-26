import pygame
from pygame.sprite import Sprite


class Koopa(Sprite):
    def __init__(self, screen):
        super(Koopa, self).__init__()
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
        self.moving_right = False
        self.moving_left = True

        # Set state
        self.in_shell = False
        self.shell_timer = 25

    def update(self):
        """Update Koopa position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.rect.right == self.screen_rect.right:
            self.moving_right = False
            self.moving_left = True
        if self.rect.left == 0:
            self.moving_right = True
            self.moving_left = False

    def blitme(self):
        """Draw Koopaa to the screen"""
        self.screen.blit(self.image, self.rect)
        pass
