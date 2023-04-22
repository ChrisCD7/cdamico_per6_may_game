# file created by Chris DAmico


# Sources: http://kidscancode.org/blog/2016/08/pg_1-1_getting-started/
# Sources: 
# testing github changes

'''
Goals:
Plane Mobs (fly horazontally across the screen)
player gets taken off screen if hit (dies)


'''
# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

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

# create game class in order to pass properties to the sprites file
############### Game Class ################
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0
        self.cd = Cooldown()
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.plane = pg.sprite.Group()
        self.bounceboy = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plane)
        
        self.all_sprites.add(self.plat1)

        self.platforms.add(self.plat1)
        
        self.all_sprites.add(self.player)


        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        for i in range(0,10):
            b = Bouncyboy(self, 20, 20, RED)
            self.all_sprites.add(b)
            self.enemies.add(b)
        for i in range(0,5):
            p = Plane(self, 20, 20, RED)
            self.all_sprites.add(p)
            self.enemies.add(p)

        # for i in range(0,14):
        #     p = P_mob(20,20,(0,0,0), self.game)
        #     self.all_sprites.add(p)
        #     self.enemies.add(p)
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
    ############ Update ##############
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
                elif hits[0].variant == "winner" and len(self.enemies) == 0:
                    self.win = True
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
        self.cd.ticking()
        if hits:
            if hits[0].variant == "normal":
                        self.player.pos.y = hits[0].rect.top
                        self.player.vel.y = 0
            elif hits[0].variant == "icy":
                        PLAYER_FRICTION = 0
                        self.player.pos.y = hits[0].rect.top
                        self.player.vel.y = 0
            elif hits[0].variant == "disappearing":
                    hits[0].kill()
            elif hits[0].variant == "bouncy":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                # elif hits[0].variant == "pmob":
                #     self.player.pos.y = hits[0].rect.top
                #     self.player.vel.y = MOB_JUMP

    ############ Draw ##############
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
    ############# Text #############
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
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