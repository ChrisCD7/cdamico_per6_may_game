import pygame as pg

from pygame.sprite import Sprite

from settings import *

from random import randint

vec = pg.math.Vector2

# player class

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH/2, HEIGHT/2
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.confric = 0.5
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()

        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        elif keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        elif keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        elif keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.pos.x = 0
        if self.rect.y > HEIGHT:
            self.pos.y = 0
        if self.rect.x < 0:
            self.pos.x = 800
        if self.rect.y < 0:
            self.pos.y = 600
    def update(self):
        self.inbounds()
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos 

class Mob(Sprite):
    def __init__(self,width,height):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(3,3)
        self.acc = vec(1,1)
        self.cofric = 0.01
    # ...
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
        if self.rect.y < 0:
            self.vel.y *= -1
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        self.pos += self.vel
        self.rect.center = self.pos
        # self.pos.y += self.vel.y