import pygame
from pygame.sprite import Sprite
import constants as c


class Mario(Sprite):
    def __init__(self, screen):
        super(Mario, self).__init__()
        self.screen = screen

        # Load Mario standing image
        self.image = pygame.image.load('images/mario/stand_right.png')
        self.walk_left = [pygame.image.load('images/mario/walk_left_1.png'),
                          pygame.image.load('images/mario/walk_left_2.png'),
                          pygame.image.load('images/mario/walk_left_3.png')]
        self.walk_right = [pygame.image.load('images/mario/walk_right_1.png'),
                           pygame.image.load('images/mario/walk_right_2.png'),
                           pygame.image.load('images/mario/walk_right_3.png')]
        self.jump_left = pygame.image.load('images/mario/jump_left.png')
        self.jump_right = pygame.image.load('images/mario/jump_right.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Position Mario
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 25

        # Store decimal value of Mario's position
        self.center = float(self.rect.centerx)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.jump_timer = 0
        self.falling = False

        # Animation Tracker
        self.walk_count = 0

    def update(self):
        """Update Mario's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right and self.rect.centerx <= c.SCREEN_WIDTH/2:
            self.rect.centerx += 3
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 3
        if self.falling and self.rect.bottom < self.screen_rect.bottom - 25:
            self.jumping = False
            self.rect.bottom += max(1.0, -0.05 * ((self.jump_timer / 10) ** 2) + 5)
            self.jump_timer -= 1
            if self.rect.bottom >= self.screen_rect.bottom - 25:
                self.rect.bottom = self.screen_rect.bottom - 25
                self.falling = False
        if self.jumping and self.rect.top > 0:
            self.falling = False
            self.rect.bottom -= -0.05 * ((self.jump_timer / 20) ** 2) + 5
            self.jump_timer -= 1
            if self.jump_timer == 0:
                self.jumping = False
                self.reset_jump_timer()
                self.falling = True

    def reset_jump_timer(self):
        self.jump_timer = 25

    def blitme(self, screen):
        """Draw Mario to the screen"""
        if self.walk_count + 1 >= 45:
            self.walk_count = 0

        if self.moving_left:
            if self.jumping:
                screen.blit(self.jump_left, self.rect)
            else:
                screen.blit(self.walk_left[self.walk_count // 15], self.rect)
            self.walk_count += 1
        elif self.moving_right:
            if self.jumping:
                screen.blit(self.jump_right, self.rect)
            else:
                screen.blit(self.walk_right[self.walk_count // 15], self.rect)
            self.walk_count += 1
        else:
            self.screen.blit(self.image, self.rect)
        pass
