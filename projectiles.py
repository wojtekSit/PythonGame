import pygame
from pygame.locals import *


class projectile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load("bullet.png").convert_alpha()
        img.set_colorkey((255, 255, 255))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.movey = 0
        self.movex = 0

    def move(self, y, x):
        self.movey -=y
        self.movex -=x

    def update(self):
        self.rect.y = self.rect.y + self.movey
        self.rect.x = self.rect.x + self.movex
    
    def shooting(self, key):
        if key == pygame.K_UP:
            self.move(8,0)
        if key == pygame.K_DOWN:
            self.move(-8,0)
        if key == pygame.K_RIGHT:
            self.move(0,-8)
        if key == pygame.K_LEFT:
            self.move(0,8)
    
    def cross_shooting1(self, key):
        if key == pygame.K_UP:
            self.move(8,0)
        if key == pygame.K_DOWN:
            self.move(-8,0)
        if key == pygame.K_RIGHT:
            self.move(0,-8)
        if key == pygame.K_LEFT:
            self.move(0,8)
    
    def cross_shooting2(self, key):
        if key == pygame.K_UP:
            self.move(-8,0)
        if key == pygame.K_DOWN:
            self.move(8,0)
        if key == pygame.K_RIGHT:
            self.move(0,8)
        if key == pygame.K_LEFT:
            self.move(0,-8)

    def cross_shooting3(self, key):
        if key == pygame.K_UP:
            self.move(0,8)
        if key == pygame.K_DOWN:
            self.move(0,8)
        if key == pygame.K_RIGHT:
            self.move(8,0)
        if key == pygame.K_LEFT:
            self.move(8,0)

    def cross_shooting4(self, key):
        if key == pygame.K_UP:
            self.move(0,-8)
        if key == pygame.K_DOWN:
            self.move(0,-8)
        if key == pygame.K_RIGHT:
            self.move(-8,0)
        if key == pygame.K_LEFT:
            self.move(-8,0)
        
    def boss_shooting(self, x, y):
        '''if x == 10 and y <830:'''
        self.move(8,8)
        
    '''def boss_shooting(self, key):
        if key == pygame.K_UP:
            self.move(8,0)
        if key == pygame.K_DOWN:
            self.move(-8,0)
        if key == pygame.K_RIGHT:
            self.move(0,-8)
        if key == pygame.K_LEFT:
            self.move(0,8)
    
    def boss_shooting(self, key):
        if key == pygame.K_UP:
            self.move(8,0)
        if key == pygame.K_DOWN:
            self.move(-8,0)
        if key == pygame.K_RIGHT:
            self.move(0,-8)
        if key == pygame.K_LEFT:
            self.move(0,8)'''
    
    def upgraded_bullets(self):
        img = pygame.image.load("upgradedbullet.png").convert_alpha()
        self.images.append(img)
        self.image = self.images[1]
    
    def default_bullets(self):
        self.image = self.images[0]
        