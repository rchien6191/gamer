#This file is by Robert Chien
#Some material taken from KidsCanCode and Mr. Cozort
#http://kidscancode.org/blog/2016/08/pygame_shmup_part_4/ <--- see this!

import pygame as pg
import random
from settings import *
from sprites import *
from os import path

#img_dir = path.join(path.dirname(__file__), '_images')
#player_img = pg.image.load(r'C:\Users\Robert.Chien19\OneDrive - Bellarmine College Preparatory\intro_to_programming\chien_robert\_images\playership.gif')

class Game:
    def __init__(self):
        #init game window
        #Init pygame
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("flying")
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        self.playersprite = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player()
        self.pbullets = PBullet()
        #Fix
        for i in range(20):
            m = Stars()
            self.all_sprites.add(m)
        for i in range (8):   
            r = SmallRocks()
            self.enemies.add(r)
            self.all_sprites.add(r)
        self.playersprite.add(self.player)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.pbullets)
        self.run()
        #New player element
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        #Game loop
    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            print("took damage")
        #Update things
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        #Listening for user input/events
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def show_start_screen(self):
        pass
    def show_go (self):
        pass
g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_start_screen()