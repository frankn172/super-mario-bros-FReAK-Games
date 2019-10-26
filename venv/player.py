import pygame
from pygame.sprite import Sprite


class Mario(Sprite):
    def __init__(self, screen):
        super(Mario, self).__init__()
        self.screen = screen

        # Load Mario standing image
        self.image = pygame.image.load('images/standing/mario_stand0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Position Mario
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value of Mario's position
        self.center = float(self.rect.centerx)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.jump_timer = 0
        self.falling = False

    def update(self):
        """Update Mario's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 3
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 3
        if self.falling and self.rect.bottom < self.screen_rect.bottom:
            self.jumping = False
            self.rect.bottom += max(1.0, -0.05 * ((self.jump_timer/10) ** 2) + 5)
            self.jump_timer -= 1
            if self.rect.bottom >= self.screen_rect.bottom:
                self.rect.bottom = self.screen_rect.bottom
                self.falling = False
        if self.jumping and self.rect.top > 0:
            self.falling = False
            self.rect.bottom -= -0.05 * ((self.jump_timer/20) ** 2) + 5
            self.jump_timer -= 1
            if self.jump_timer == 0:
                self.jumping = False
                self.reset_jump_timer()
                self.falling = True

    def reset_jump_timer(self):
        self.jump_timer = 25

    def blitme(self):
        """Draw Mario to the screen"""
        self.screen.blit(self.image, self.rect)
        pass
