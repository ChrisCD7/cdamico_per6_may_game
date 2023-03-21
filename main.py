# file created by Chris DAmico


# Sources: http://kidscancode.org/blog/2016/08/pg_1-1_getting-started/
# Sources: 
# testing github changes

# import libs
import pygame as pg
import random
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)

# init pg and create window
pg.init()
# init sound mixer
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My first game...")
clock = pg.time.Clock() 


all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player()

all_sprites.add(player)
player.pos = 0,0
# for loop creates mobs
for i in range(0,150):
    # instantiate 20 mobs
    m = Mob(randint(30,90), randint(30,90), randint(0,100))
    enemies.add(m)
    all_sprites.add(m)

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('times new roman')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

# game loop

while RUNNING:
    #  keep loop running at the right speed
    clock.tick(FPS)
    ### process input events section of game loop
    for event in pg.event.get():
        # check for window closing
        if event.type == pg.QUIT:
            RUNNING = False
        if event.type == pg.KEYDOWN:
            if event.type == pg.K_ESCAPE:
                PAUSED = True
            # break
    # print(get_mouse_now())
    ### update section of game loop (if updates take longer the 1/30th of a second, you will get laaaaag...)
   
    ################ PAUSE #################
    keystate = pg.key.get_pressed()

    if keystate[pg.K_ESCAPE]:
        PAUSED = True
    if not PAUSED:
        all_sprites.update()
        enemies.update()
    elif PAUSED == True:
        keystate[pg.K_ESCAPE]
        PAUSED = False
    ########## collision ############
    blocks_hit_list = pg.sprite.spritecollide(player, enemies, True)
    if blocks_hit_list:
        SCORE += 1
    
    for block in blocks_hit_list:
        # print(enemies)
        pass

    
        

    ### draw and render section of game loop
    screen.fill(BLUE)
    draw_text("Score: " + str(SCORE), 22, WHITE, 35, 0)
    # if blocks_hit_list:

    all_sprites.draw(screen)
    # double buffering draws frames for entire screen
    pg.display.flip()
    # pg.display.update() -> only updates a portion of the screen
# ends program when loops evaluates to false
pg.quit()