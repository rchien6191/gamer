#Sprites for the game!
#Taken from kenney.nl

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *
import math
import os

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #player_img = pg.image.load(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\project\gamer\_assets\playership2.png')
        #I'm not sure what the 'r' before the filepath does but it only really works with the 'r'?
        #It was part of some advice on stackoverflow.
        
        # Want to shrink down the filepath so it works generally across other computers, see below for example?
        #player_img = pg.image.load('\_assets\playership2.png')
        #solved!
        player_img = pg.image.load(os.path.join('_assets', 'playership2.png'))

        #shoot_sound = pg.mixer.Sound(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\_assets\laser4.wav')
        self.image = player_img
        self.image = pg.transform.scale(player_img, (40, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, (3*HEIGHT)/4)
        self.radius = 15
        #pg.draw.circle(self.image, WHITE, self.rect.center, self.radius)
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
        self.bullet.rect.x = self.player.rect.x + 16
        self.bullet.rect.y = self.player.rect.y
        #I don't know how this works but it works so I'll take it
        #How is python recognizing what 'self' is referring to? There's red marks all over it. 

class PBullet(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        playerlaser = pg.image.load(os.path.join('_assets', 'laserp.png'))
        #playerlaser = pg.image.load(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\project\gamer\_assets\laserp.png')
        self.image = playerlaser
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.rect.y
        self.rect.centerx = self.rect.x
        self.vy = -25
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
        #smallrock_img = pg.image.load(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\project\gamer\_assets\spacerock.png')
        smallrock_img = pg.image.load(os.path.join('_assets', 'spacerock.png'))
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
        self.radius = int(self.rect.width / 2)
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
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
            self.image.set_colorkey(BLACK)

class Enemy1(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #enemy1img = pg.image.load(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\project\gamer\_assets\enemy1.png')
        enemy1img = pg.image.load(os.path.join('_assets', 'enemy1.png'))
        self.image = enemy1img
        self.image = pg.transform.scale(enemy1img, (30, 30))
        self.image.set_colorkey(BLACK)
        self.radius = 15
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-450, -50)
        self.vy = random.randrange(4, 8)
        self.vx = random.randrange(-2, 2)
        #Debating if I should add shooting to the enemies too. It's hard enough already with ~20 obstacles on screen.
    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -20 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-450, -50)
            self.vy = random.randrange(4, 8)
            self.vx = random.randrange(-2, 2)


#Explosions. Adapted from kidscancode, mostly. 
#for loop loads regularExplosion0{}.png, with numbers 0-9 in {}, then adds them to explosion_anim['fire'] list
explosion_anim = {}
explosion_anim['fire'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pg.image.load(os.path.join('_assets\explosions', filename))
    img.set_colorkey(BLACK)
    img_fire = pg.transform.scale(img, (35, 35))
    explosion_anim['fire'].append(img_fire)
#Why 'fire': plan to have a different, more "dusty" break animation for the rocks
#Just not sure where to find one or how to make one....

class Explosion(pg.sprite.Sprite):
    def __init__(self, center, size):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50
#Runs through the individual frames based on framerate: above is setup, as always
    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            #Progress through the frames/images one at a time. 
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
                #When the frames run out, kill the sprite
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                #coordinate where the frames center, which should be the the site of ship destruction.