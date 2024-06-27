from re import X
import pygame
from Sprite import Player
from pygame.locals import *
import math
from pygame.constants import KEYDOWN


screen_rect = pygame.Rect((0, 0), (1000, 1000))

class enemy(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            img = pygame.image.load("Enemy.png").convert_alpha()
            img.set_colorkey((255, 255 ,255))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def following(self):
        
        if self.rect.x < Player.rect.x:
            self.rect.x += 1
        elif self.rect.x == Player.rect.x:    
            self.rect.x += 0 
        else:
            self.rect.x -= 1
        if self.rect.y < Player.rect.y:
            self.rect.y += 1
        elif self.rect.y == Player.rect.y:
            self.rect.y -= 0
        else:
            self.rect.y -= 1
        self.rect.clamp_ip(screen_rect)
    

        
        
        