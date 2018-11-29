#Sprites for the game!
#Taken from kenney.nl

import pygame as pg
from pygame.sprite import Sprite
import random
#import main
from settings import *
import math
from os import path

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #self.image = pg.image.load(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\_images\playership.gif')
        self.image = pg.Surface((30, 30))
        #self.sprite = player_img
        
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        #self.sprite = self.image.get_image()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        #Sprite will be implemented at some point
        self.accel = 3.95
        self.vx = 0
        self.vy = 0

    def shoot(self):
        bullet = PBullet(self.rect.x, self.rect.y)
        Game.all_sprites.add(bullet)
        Game.pbullets.add(bullet)

    def update(self):
        self.vx = 0
        self.vy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -7
        if keys[pg.K_RIGHT]:
            self.vx = 7
        if keys[pg.K_UP]:
            self.vy = -7
        if keys[pg.K_DOWN]:
            self.vy = 7
        if keys[pg.K_SPACE]:
            self.shoot()
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class PBullet(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((3, 5))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.vy = -15
    def update(self):
        self.rect.y += self.vy
        if self.rect.y < 0 :
            self.kill()



class Stars(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((2, 2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-600, 0)
        self.vy = random.randrange(25, 28)
    def update(self):
        self.rect.y += self.vy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.vy = random.randrange(25, 29)


class SmallRocks(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-450, -50)
        self.vy = random.randrange(3, 8)
    def update(self):
        self.rect.y += self.vy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-450, -50)
            self.vy = random.randrange(3, 8)