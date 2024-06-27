import pygame

pygame.init()

class damageflash(pygame.sprite.Sprite):       
    
    def __init__(self, x1, y1):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load("damageflash.png").convert_alpha()
        img.set_colorkey((255, 255 ,255))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
   



        

