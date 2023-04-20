# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
from math import *
from math import ceil
from os import path
from random import choice

# player class


class Cooldown():
    def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
    def ticking(self):
        self.current_time = floor((pg.time.get_ticks())/1000)
        self.delta = self.current_time - self.event_time
        # print(self.delta)
    def reset(self):
        self.event_time = floor((pg.time.get_ticks())/1000)
    def timer(self):
        self.current_time = floor((pg.time.get_ticks())/1000)


class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        self.score = 0
        self.win = False
        self.lose = False
    
    # to add images sounds etc copy below...and add this to the new method below...
    # def load_data(self):
    #     self.player_img = pg.image.load(path.join(img_folder, "bellar_man_single_frm.png")).convert()

    def new(self):
        # starting a new game
        self.score = 0

        # added to load data
        # self.load_data()

        self.cd = Cooldown()
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.plat_list = []
        self.enemies = pg.sprite.Group()
        self.attached_items = pg.sprite.Group()
        self.player = Player(self)
        # self.coin1 = Coin(asdfasdf)
        # self.all_sprites.add(coin1)
        # self.coins.add(coin1)
        self.plat1 = Platform(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal")
        self.all_sprites.add(self.player)

        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        
        
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # for i in range(0,15):
        #     p = Platform(randint(0,WIDTH-50), randint(0,HEIGHT-50), 100, 25, BLACK, "normal")
        #     self.all_sprites.add(p)
        #     self.platforms.add(p)
        #     self.plat_list.append(p)
        for plat in self.plat_list:
            x = 0
            while (abs(plat.rect.x - self.plat_list[self.plat_list.index(plat)-x].rect.x) < 200 and
                abs(plat.rect.y - self.plat_list[self.plat_list.index(plat)-x].rect.y) < 50 ):
                print("i need to adjust this platform...") 
                plat.rect.x += 50
                plat.rect.y += 50
                x += 1
            # plat.image.fill((x*10, 255, 255))

        for i in range(0,10):
            m = Mob(20,20,(255,50,50))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.start_score = len(self.platforms)
        # self.cd.timer()
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        # checking to see if timer has run out  
        if self.cd.delta > 10:
            pass
            # print("you ran out of time and you lose!")
        
        # check to see if we collide with enemyd
        mhits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if mhits:
            self.cd.reset()
          
            # self.player.health -= 10a
            mhits[0].attached_now = True
            self.enemies.remove(mhits[0])
            self.attached_items.add(mhits[0])
            self.score -= 1
        # if mhits:
        #     if self.player.vel.x < 0:
        #         self.player.pos.x += 5
        #     if self.player.vel.x > 0:
        #         self.player.pos.x -= 5
        #     if self.player.vel.y > 0:
        #         self.player.pos.y -= 5
            
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                
                if abs(self.player.vel.x) > abs(self.player.vel.y):
                    if self.player.vel.x > 0:
                        pass
                        # print("Im going faster on the x and coming from the left...")
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                elif hits[0].variant == "winner" and len(self.enemies) == 0:
                    self.win = True
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
        self.cd.ticking()

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        if self.player.vel.x > 5: 
            # self.draw_health_bar(self.screen, self.player.rect.x-18, self.player.rect.y -25, self.player.health)
            self.draw_text(str(self.cd.delta), 24, WHITE, 50, 50)
        if self.cd.delta > 10:
            if self.score > 5:
                self.draw_text("if you win...", 24, WHITE, WIDTH/2, 100)
            else:
                self.draw_text("you lose...", 24, WHITE, WIDTH/2, 100)

        if not self.win:
            # self.draw_text(str(self.player.rot), 24, WHITE, WIDTH/2, HEIGHT/2)
            self.draw_text(str(self.score), 24, WHITE, WIDTH/2, HEIGHT/2)
        else:
            self.draw_text("You win!", 24, WHITE, WIDTH/2, HEIGHT/2)

        # is this a method or a function?
        pg.display.flip()
    
    # def draw_health_bar(self, surf, x, y, pct):
    #     if pct < 0:
    #         pct = 0
    #     BAR_LENGTH = 100
    #     BAR_HEIGHT = 10
    #     fill = (pct / 100) * BAR_LENGTH
    #     outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    #     fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    #     pg.draw.rect(surf, RED, fill_rect)
    #     pg.draw.rect(surf, WHITE, outline_rect, 2)

    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('comic sans')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()