#Sprites for the game!

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *
import math

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        # self.pos = vec(WIDTH/2, HEIGHT/2)
        # self.velo = vec(0, 0)
        # self.accel = vec(0,0)
        self.accel = 3.95
        self.vx = 0
        self.vy = 0
        self.falling = False
    def jumping(self):
        self.vy = -50
        print("jump called")
        self.falling = True
    def gravity(self):
        if self.rect.y < HEIGHT-30:
            self.falling = True
            self.vy += self.accel
            #print("Falling" + str(self.falling))
        elif self.rect.y > HEIGHT:
            self.falling = False
            self.vy = 0
            self.rect.y = HEIGHT-30
            print("Falling" + str(self.falling))
    def update(self):
        self.vx = 0
        #self.vy = 0
        self.gravity()
        #self.jumping()
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -7
        if keys[pg.K_RIGHT]:
            self.vx = 7
        if keys[pg.K_UP] and self.falling == False:
            self.jumping()
        self.rect.x += self.vx
        self.rect.y += self.vy
        # if self.rect.colliderect(Platforms.rect):



class Platforms(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((60, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.vx = 0
        self.vy = 0