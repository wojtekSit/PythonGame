from re import X
from turtle import position
import pygame
from pygame.constants import KEYDOWN
import math
from pygame.locals import *

pygame.init()

screen_rect = pygame.Rect((0, 0), (1000, 1000))

class Player(pygame.sprite.Sprite):
       
    def __init__(self, x1, y1):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        Player.img = pygame.image.load("player.png").convert_alpha()
        Player.img.set_colorkey((255, 255 ,255))
        self.images.append(Player.img)
        self.image = self.images[0]
        Player.rect = self.image.get_rect()
        Player.rect.x = x1
        Player.rect.y = y1
    
    def moving(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            Player.rect.x -= 5
        if keys_pressed[pygame.K_d]:
            Player.rect.x += 5
        if keys_pressed[pygame.K_w]:
            Player.rect.y -= 5
        if keys_pressed[pygame.K_s]:
            Player.rect.y += 5
        Player.rect.clamp_ip(screen_rect)
        