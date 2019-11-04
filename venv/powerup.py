import pygame as pg

import constants as c


class Powerup(pg.sprite.Sprite):
    """Superclass of all powerups"""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.direction = None
        self.state = None

        self.gravity = None

        self.image = None
        self.rect = None

        self.x_vel = None
        self.y_vel = None

    def setup_enemy(self, x, y, direction, image):
        """Set up powerup values"""
        self.direction = direction
        self.state = c.WALK
        self.gravity = 1.5

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.set_velocity()

    def set_velocity(self):
        """Set velocity"""
        if self.direction == c.LEFT:
            self.x_vel = -2
        else:
            self.x_vel = 2

        self.y_vel = 0

    def handle_state(self):
        """Powerup behavior is based on what state it is in"""
        if self.state == c.WALK:
            self.walking()
        elif self.state == c.FALL:
            self.falling()

    def walking(self):
        """Default state of moving from side to side"""
        self.rect.x += self.x_vel
        if self.rect.left == 0:
            self.direction = c.RIGHT
            self.set_velocity()
        if self.rect.right == c.SCREEN_WIDTH:
            self.direction = c.LEFT
            self.set_velocity()

    def falling(self):
        if self.y_vel < 10:
            self.y_vel += self.gravity
        if self.rect.bottom >= c.GROUND_HEIGHT:
            # self.rect.y == c.GROUND_HEIGHT
            self.y_vel = 0
            self.state = c.WALK
            return
        self.rect.y += self.y_vel

    def update(self, *args):
        self.handle_state()


class Mushroom(Powerup):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT):
        Powerup.__init__(self)
        image = pg.image.load('images/Cut-Sprites-For-Mario/Items/10.png')
        self.setup_enemy(x, y, direction, image)


class Flower(Powerup):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT):
        Powerup.__init__(self)
        image = pg.image.load('images/Cut-Sprites-For-Mario/Items/17.png')
        self.setup_enemy(x, y, direction, image)

    def walking(self):
        return


class Life(Powerup):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT):
        Powerup.__init__(self)
        image = pg.image.load('images/Cut-Sprites-For-Mario/Items/12.png')
        self.setup_enemy(x, y, direction, image)


class Star(Powerup):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT):
        Powerup.__init__(self)
        image = pg.image.load('images/Cut-Sprites-For-Mario/Items/23.png')
        self.setup_enemy(x, y, direction, image)
        self.y_vel = -5

    def walking(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        if self.rect.left == 0:
            self.direction = c.RIGHT
            self.set_velocity()
        if self.rect.right == 300:
            self.direction = c.LEFT
            self.set_velocity()
        if self.falling:
            if self.y_vel < 6:
                self.y_vel += self.gravity
            if self.rect.bottom >= c.GROUND_HEIGHT:
                # self.rect.y == c.GROUND_HEIGHT
                self.y_vel = -6
            self.rect.y += self.y_vel

    def set_velocity(self):
        """Set velocity"""
        if self.direction == c.LEFT:
            self.x_vel = -2
        else:
            self.x_vel = 2
