from math import cos
from math import pi
from math import sin

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
        self.invulnerable_timer = None
        self.is_invulnerable = None
        self.state = None

        self.name = None
        self.direction = None

        self.image = None
        self.rect = None

        # Walking Counter
        self.walk_count = 0

        self.x_vel = None
        self.y_vel = None

    def setup_enemy(self, x, y, direction, name, setup_frames):
        """Set up enemies values"""
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.invulnerable_timer = 0
        self.is_invulnerable = False
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
        if self.is_invulnerable:
            self.invulnerable_timer += 1
            if self.invulnerable_timer == 100:
                self.invulnerable_timer = 0
                self.is_invulnerable = False
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
        elif self.state == c.FLYING:
            self.flying()
        elif self.state == c.WAIT:
            self.waiting()

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
        if self.rect.bottom >= c.GROUND_HEIGHT:
            self.rect.y == c.GROUND_HEIGHT
            self.y_vel = 0
            self.state = c.WALK
            return
        self.rect.y += self.y_vel

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

    def draw(self, screen):
        pass


class Goomba(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name='goomba'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        self.walk = [pg.image.load('images/Cut-Sprites-For-Mario/Enemies/76.png'),
                     pg.image.load('images/Cut-Sprites-For-Mario/Enemies/72.png')]

    def setup_frames(self):
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/76.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/72.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/73.png'))

    def jumped_on(self):
        self.frame_index = 2
        self.kill()

    def draw(self, screen):
        if self.walk_count + 1 >= 40:
            self.walk_count = 0

        screen.blit(self.walk[self.walk_count // 20], self.rect)
        self.walk_count += 1


class Koopa(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name="koopa", winged=False):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        self.winged = winged
        self.max_height = y - 50
        self.min_height = y + 50
        if winged:
            self.state = c.FLYING
            self.y_vel = -1
        self.inShell = False

        # Animation
        self.walk_left = [pg.image.load('images/Cut-Sprites-For-Mario/Enemies/87.png'),
                          pg.image.load('images/Cut-Sprites-For-Mario/Enemies/96.png')]
        self.walk_right = [pg.image.load('images/Cut-Sprites-For-Mario/Enemies/106.png'),
                           pg.image.load('images/Cut-Sprites-For-Mario/Enemies/97.png')]

    def setup_frames(self):
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/87.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/96.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/118.png'))

    def jumped_on(self):
        """When Mario jumps on the Koopa, he should enter his shell"""
        if self.winged:
            self.winged = False
            self.state = c.FALL
            self.y_vel = 0
            self.is_invulnerable = True
            return
        if self.inShell and not self.is_invulnerable:
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
        self.is_invulnerable = True

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

    def flying(self):
        if self.rect.y <= self.max_height or self.rect.y >= self.min_height:
            self.y_vel = self.y_vel * -1
        self.rect.y += self.y_vel

    def draw(self, screen):
        if self.walk_count + 1 >= 40:
            self.walk_count = 0

        if self.direction == c.LEFT:
            screen.blit(self.walk_left[self.walk_count // 20], self.rect)
            self.walk_count += 1
        else:
            screen.blit(self.walk_right[self.walk_count // 20], self.rect)
            self.walk_count += 1


class PirahnaPlant(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name="plant"):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        self.y_vel = -1
        self.max_height = y - 50
        self.min_height = y
        self.pipe_timer = 0
        self.animate = [pg.image.load('images/Cut-Sprites-For-Mario/Enemies/123.png'),
                        pg.image.load('images/Cut-Sprites-For-Mario/Enemies/120.png')]

    def setup_frames(self):
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/123.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/120.png'))

    def jumped_on(self):
        """When Mario jumps on the Pirahana Plant, Mario should get shrink or die"""
        self.state = c.WALK

    def walking(self):
        self.rect.y += self.y_vel
        if self.rect.y <= self.max_height or self.rect.y >= self.min_height:
            self.y_vel = self.y_vel * -1
            if self.rect.y >= self.min_height:
                self.state = c.WAIT

    def waiting(self):
        if self.pipe_timer == 100:
            self.pipe_timer = 0
            self.state = c.WALK
        else:
            self.pipe_timer += 1

    def draw(self, screen):
        if self.walk_count + 1 >= 40:
            self.walk_count = 0

        screen.blit(self.animate[self.walk_count // 20], self.rect)
        self.walk_count += 1


class CheepCheep(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT / 2, x=0, direction=c.LEFT, name='cheepcheep'):
        # TODO, makes two types of cheepcheeps, the gray variety moves faster than the green
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        self.swim_left = [pg.image.load('images/Cut-Sprites-For-Mario/Enemies/23.png'),
                          pg.image.load('images/Cut-Sprites-For-Mario/Enemies/22.png')]
        self.swim_right = [pg.image.load('images/Cut-Sprites-For-Mario/Enemies/24.png'),
                           pg.image.load('images/Cut-Sprites-For-Mario/Enemies/25.png')]

    def setup_frames(self):
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/23.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/23.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/73.png'))

    def jumped_on(self):
        self.frame_index = 2
        self.kill()

    def draw(self, screen):
        if self.walk_count + 1 >= 40:
            self.walk_count = 0

        if self.direction == c.LEFT:
            screen.blit(self.swim_left[self.walk_count // 20], self.rect)
            self.walk_count += 1
        elif self.direction == c.RIGHT:
            screen.blit(self.swim_right[self.walk_count // 20], self.rect)
            self.walk_count += 1


class FireBar(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT / 2, x=0, direction=c.LEFT, name='firebar', radius=10):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = 0

    def setup_frames(self):
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/60.png'))

    def jumped_on(self):
        self.state = c.WALK

    def walking(self):
        self.angle += pi / 64
        self.rect.x = cos(self.angle) * self.radius + self.x
        self.rect.y = sin(self.angle) * self.radius + self.y

    def draw(self, screen):
        screen.blit(self.frames[0], self.rect)


class Podaboo(Enemy):
    def __init__(self, y=c.GROUND_HEIGHT - 10, x=0, direction=c.LEFT, name="podaboo"):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        self.y_vel = -1
        self.max_height = y - 100
        self.min_height = y
        self.pipe_timer = 0

        self.move_up = pg.image.load('images/Cut-Sprites-For-Mario/Enemies/61.png')
        self.move_down = pg.image.load('images/Cut-Sprites-For-Mario/Enemies/56.png')

    def setup_frames(self):
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/56.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/61.png'))

    def jumped_on(self):
        """When Mario jumps on the Pirahana Plant, Mario should get shrink or die"""
        self.state = c.WALK

    def walking(self):
        self.rect.y += self.y_vel
        if self.rect.y <= self.max_height or self.rect.y >= self.min_height:
            self.y_vel = self.y_vel * -1
            if self.rect.y >= self.min_height:
                self.state = c.WAIT

    def waiting(self):
        if self.pipe_timer == 100:
            self.pipe_timer = 0
            self.state = c.WALK
        else:
            self.pipe_timer += 1

    def draw(self, screen):
        if self.y_vel > 0:
            screen.blit(self.move_up, self.rect)
        else:
            screen.blit(self.move_down, self.rect)


class Blooper(Enemy):
    def __init__(self, mario, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name="blooper"):
        Enemy.__init__(self)
        self.mario = mario
        self.setup_enemy(x, y, direction, name, self.setup_frames)
        self.y_vel = -1
        self.x_vel = 0
        self.max_height = y - 50
        self.min_height = y
        self.pipe_timer = 0
        self.move_down = False
        self.move_up = False

        # Animation List
        self.animate = [pg.image.load('images/Cut-Sprites-For-Mario/Enemies/119.png'),
                        pg.image.load('images/Cut-Sprites-For-Mario/Enemies/124.png')]

    def setup_frames(self):
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/124.png'))
        self.frames.append(pg.image.load('images/Cut-Sprites-For-Mario/Enemies/119.png'))

    def jumped_on(self):
        """When Mario jumps on the Pirahana Plant, Mario should get shrink or die"""
        self.state = c.WALK

    def walking(self):
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel

        if self.mario.rect.centerx == self.rect.centerx:
            self.x_vel = 0

        if self.rect.y <= self.max_height:
            self.y_vel = self.y_vel * -1
            self.move_down = True
            self.move_up = False
            if self.mario.rect.centerx < self.rect.centerx:
                self.x_vel = -1
            elif self.mario.rect.centerx > self.rect.centerx:
                self.x_vel = 1
            else:
                self.x_vel = 0
        elif self.rect.y >= self.min_height:
            self.move_down = False
            self.move_up = True
            self.y_vel = self.y_vel * -1
            self.x_vel = 0

    def draw(self, screen):
        if self.move_down:
            screen.blit(self.animate[0], self.rect)
        else:
            screen.blit(self.animate[1], self.rect)
