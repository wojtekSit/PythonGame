import pygame
from Sprite import Player
from pygame.constants import KEYDOWN

screen_rect = pygame.Rect((0, 0), (1000, 1000))

class boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("boss.png").convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = pygame.mask.Mask.get_rect(self.mask)
            self.rect.x = x
            self.rect.y = y

    def following(self):
        if self.rect.x == 10 and self.rect.y < 830:
            if self.rect.y == 829:
                self.rect.x +=1
            self.rect.y += 3
        if self.rect.x < 831 and self.rect.y == 829:
            if self.rect.x == 829:
                self.rect.y +=1
            self.rect.x += 3
        if self.rect.x == 829 and self.rect.y <830:
            if self.rect.y == 10:
                self.rect.x -=1
            self.rect.y -= 3
        if self.rect.x < 830 and self.rect.y == 10:
            if self.rect.x == 10:
                self.rect.y -=1
            self.rect.x -= 3
