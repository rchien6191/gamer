#This file is by Robert Chien
#Some material taken from KidsCanCode and Mr. Cozort
#Now on github

import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        #init game window
        #Init pygame
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("jumping")
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.platform = Platforms()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.platform)
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
        #Update things
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        #Listening for user input/events
    def draw(self):
        self.screen.fill(RED)
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