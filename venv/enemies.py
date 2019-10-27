import pygame as pg
import constants as c


class Enemy(pg.sprite.Sprite):
    """Superclass of all enemies"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.frames = None
        self.frame_index = None
        self.animate_timer = None
        self.death_timer = None
        self.gravity = None
        self.state = None

        self.name = None
        self.direction = None

        self.image = None
        self.rect = None

        self.x_vel = None
        self.y_vel = None

    def setup_enemy(self, x, y, direction, name, setup_frames):
        """Set up enemies values"""
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.state = c.WALK

        self.name = name
        self.direction = direction
        setup_frames()

        self.image = self.frames[self.frame_index]
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

        # Will be used for Red Paratroopas, Podaboos, Firebars etc)
        self.y_vel = 0

    def get_image(self):
        pass

    def handle_state(self):
        """Enemy behavior is based on what state it is in"""
        if self.state == c.WALK:
            self.walking()
        elif self.state == c.FALL:
            self.falling()
        elif self.state == c.JUMPED_ON:
            self.jumped_on()
        elif self.state == c.SHELL_SLIDE:
            self.shell_sliding()
        elif self.state == c.DEATH_JUMP:
            self.death_jumping()

    def walking(self):
        """Default state of moving from side to side"""
        if self.frame_index == 0:
            self.frame_index += 1
        if self.frame_index == 1:
            self.frame_index = 1

        self.rect.x += self.x_vel
        if self.rect.left == 0:
            self.direction = c.RIGHT
            self.set_velocity()
        if self.rect.right == 300:
            self.direction = c.LEFT
            self.set_velocity()

    def falling(self):
        if self.y_vel < 10:
            self.y_vel += self.gravity

    def jumped_on(self):
        """Placeholder for when enemy is stomped on by Mario"""
        pass

    def death_jumping(self):
        """Death animation"""
        pass

    def start_death_jump(self):
        pass

    def animation(self):
        self.image = self.frames[self.frame_index]

    def update(self, *args):
        self.handle_state()
        self.animation()


class Goomba(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name='goomba'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)

    def setup_frames(self):
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/76.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/72.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/73.png'))

    def jumped_on(self):
        self.frame_index = 2
        self.kill()


class Koopa(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name="koopa"):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        self.inShell = False

    def setup_frames(self):
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/87.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/96.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/118.png'))

    def jumped_on(self):
        """When Mario jumps on the Koopa, he should enter his shell"""
        if self.inShell:
            self.state = c.SHELL_SLIDE
            return
        self.x_vel = 0
        self.frame_index = 2
        shell_y = self.rect.bottom
        shell_x = self.rect.x
        self.rect = self.frames[self.frame_index].get_rect()
        self.rect.x = shell_x
        self.rect.bottom = shell_y
        self.inShell = True

    def shell_sliding(self):
        """Define how the shell should move"""
        self.rect.x += self.x_vel
        if self.direction == c.RIGHT:
            self.x_vel = 10
        elif self.direction == c.LEFT:
            self.x_vel = -10
        if self.rect.left <= 0:
            self.direction = c.RIGHT
        if self.rect.right >= 300:
            self.direction = c.LEFT
