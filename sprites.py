#Sprites for the game!
#Taken from kenney.nl

import pygame as pg
from pygame.sprite import Sprite
import random

from settings import *
import math
from os import path

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        # playersprite = "C:\_assets\playership.png"
        # player_img = pg.image.load(playersprite)
        player_img = pg.image.load(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\project\gamer\_assets\playership.png')
        #I'm not sure what the 'r' before the filepath does but it only really works with the 'r'?
        #It was part of some advice on stackoverflow.
        #shoot_sound = pg.mixer.Sound(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\_assets\laser4.wav')
        self.image = player_img
        self.image = pg.transform.scale(player_img, (40, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, (3*HEIGHT)/4)
        self.accel = 3.95
        self.vx = 0
        self.vy = 0

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
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        #print("bang")
        self.all_sprites.add(self.bullet)
        self.pbullets.add(self.bullet)
        self.bullet.rect.x = self.player.rect.x + 17.5
        self.bullet.rect.y = self.player.rect.y

class PBullet(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((5, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.rect.y
        self.rect.centerx = self.rect.x
        self.vy = -20
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
        smallrock_img = pg.image.load(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\project\gamer\_assets\spacerock.png')
        #self.image = pg.Surface((40, 40))
        #self.image.fill(BLUE)
        self.image_orig = smallrock_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        #self.image = smallrock_img
        self.image = pg.transform.scale(smallrock_img, (40, 40))
        self.image_orig = pg.transform.scale(smallrock_img, (40, 40))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-450, -50)
        self.vy = random.randrange(3, 8)
        self.rot = 0
        self.rot_spd = random.randrange(-4, 4)
        self.last_update = pg.time.get_ticks()
    def update(self):
        self.rect.y += self.vy
        self.rotate()
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-450, -50)
            self.vy = random.randrange(3, 8)
    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_spd) % 360
            self.image = pg.transform.rotate(self.image_orig, self.rot)

class Enemy1(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-450, -50)
        self.vy = random.randrange(4, 8)
        self.vx = random.randrange(-2, 2)
    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -20 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-450, -50)
            self.vy = random.randrange(4, 8)
            self.vx = random.randrange(-2, 2)
