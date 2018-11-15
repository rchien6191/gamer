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
        self.image = pg.image.load("_images/playership.gif")
        self.image = pg.Surface((30, 30))
        #self.image.fill(RED)
        self.sprite = self.image.get_image()
        self.image.center = (WIDTH/2, HEIGHT/2)
        #The above will be replaced with a proper sprite at some point
        #Sprite will be implemented at some point
        self.accel = 3.95
        self.vx = 0
        self.vy = 0
        self.falling = False
    # def jumping(self):
    #     self.vy = -50
    #     print("jump called")
    #     self.falling = True
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
            #self.jumping()
        # else:
        #     self.vx = 0
        #     self.vy = 0
        self.rect.x += self.vx
        self.rect.y += self.vy



class Stars(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((5, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT-20)
        self.vy = 0
    def update(self):
        self.vy = 30
        if self.rect.y <= 0:
            self.rect.y == HEIGHT+20
            self.vy = 30
            self.rect.y += self.vy
        self.rect.y += self.vy
