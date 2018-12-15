#This file is by Robert Chien
#Sources: KidsCanCode and Mr. Cozort

import pygame as pg
import random
from settings import *
from sprites import *

#Gameplay ideas: schmup, two varieties of non-player mobs: asteroids (no point value) and ships (point value)
#Cosmetics: Graphics, explosion animations (ship hit), sounds?
#Planned features: score system, shooting, random spawning, difficulty scaling, animations, sounds, graphics, health system, game over screen
#Accomplished: score system, shooting, random spawning, random spawning, difficulty scaling, graphics, limited animations
#Bugs: clunky shooting mechanics (see Player class, sprites.py for more details), visual collision bugs, 


#Personal Note, 12/14/18: I thought I'd get a lot more implemented, but a surpisingly large amount of time was spent 
# troubleshooting, especially the shooting / graphics implementation

class Game:
    def __init__(self):
        #init game window
        #Init pygame
        pg.init()
        pg.mixer.init()
        pg.font.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("flying")
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        self.score = 0
        self.playersprite = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        
        self.obstacles = pg.sprite.Group()
        self.indestruct = pg.sprite.Group()
        #All the sprites and their groups. Ready for collisions.
        self.player = Player()
        self.enemy1 = Enemy1()
        self.bullet = PBullet(self.player.rect.centerx, self.player.rect.top)
        self.pbullets = pg.sprite.Group()
        for i in range(20):
            m = Stars()
            self.all_sprites.add(m)
        for i in range (10):   
            r = SmallRocks()
            self.obstacles.add(r)
            self.all_sprites.add(r)
        for i in range (4):
            s = Enemy1()
            self.enemies.add(s)
            #self.obstacles.add(s)
            self.all_sprites.add(s)
        self.playersprite.add(self.player)
        self.all_sprites.add(self.player)
        self.run()
        #New player element
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            #self.score()
            self.update()
            self.draw()
        #Game loop
    def update(self):
        #Collisions
        self.all_sprites.update()
        hits1 = pg.sprite.spritecollide(self.player, self.enemies, False, pg.sprite.collide_circle)
        hits2 = pg.sprite.spritecollide(self.player, self.obstacles, False, pg.sprite.collide_circle)
        #The hitboxes should? be better, with circle type collisions? Hard to tell, difficult to 
        # graze the rocks due to their rotations/x movement
        bulletmobhits = pg.sprite.groupcollide(self.pbullets, self.enemies, True, True)
        obstaclehits = pg.sprite.groupcollide(self.pbullets, self.obstacles, True, True)
        if hits1:
            print("took damage")
            self.running = False
            for hit in hits1:
                self.player.health -= hit.radius / 4
                if self.player.health <= 0:
                    self.running = False
        if hits2:
            print("took damage")
            print (self.player.health)
            for hit in hits2:
                self.player.health -= hit.radius / 4
                if self.player.health <= 0:
                    self.running = False
            
        if obstaclehits:
            self.bullet.kill()
            r = SmallRocks()
            self.all_sprites.add(r)
            self.obstacles.add(r)

        if bulletmobhits:
            print("impact")
            self.bullet.kill()
            for hit in bulletmobhits:
                self.score += 1
                print(self.score)
                r = SmallRocks()
                s = Enemy1()
                exp = Explosion(hit.rect.center, 'fire')
                self.all_sprites.add(exp)
                self.all_sprites.add(r)
                self.all_sprites.add(s)
                self.obstacles.add(r)
                self.enemies.add(s)
                # difficulty scaling?: Each object destroyed spawns it back as well as the other type available
                # ie: shooting a satellite spawns both a satellite and a rock, and vice versa. 
                # It gradually gets harder
            
    # def shoot(self):
    #     #print("bang")
    #     self.all_sprites.add(self.bullet)
    #     self.pbullets.add(self.bullet)
    #     self.bullet.rect.x = self.player.rect.x + 17.5
    #     self.bullet.rect.y = self.player.rect.y  

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not self.pbullets.has(self.bullet):
                    Player.shoot(self)
                    #self.shoot()
            #The shoot function here took way too long to figure out. Currently, it mostly works, but is capped to 
            #one player bullet on screen at any one time. 
            #12/13/18 I'm still not sure how it's working placed in the Player class, but I'll take it
            # If things go bad the legacy version is just above, uncomment the shoot function and self.shoot()
            #It only seems to work with the 'and not self' part tacked on, which is what's limiting the bullet count

    def draw_text(self, screen):
        #The score display
        myFont = pg.font.SysFont('monospace', 30)
        scoretext = myFont.render('Score: ' + str(self.score), False, WHITE)
        self.screen.blit(scoretext, (20,30))
    
    def draw_health_bar(self, surf, x, y, pct):
        if pct<0:
            pct = 0
            #pct: which value to measure for the rectangle drawing
        Health_length = 100
        Health_height = 10
        fill = (pct/100) * Health_length
        outline_rect = pg.Rect(x, y, Health_length, Health_height)
        fill_rect = pg.Rect(x, y, fill, Health_height)
        pg.draw.rect(surf, GREEN, fill_rect)
        pg.draw.rect(surf, WHITE, outline_rect, 2)

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen)
        self.draw_health_bar(self.screen, 400 , HEIGHT/16, self.player.health)
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