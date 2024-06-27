import pygame

pygame.init()

class shopitems(pygame.sprite.Sprite):       
    
    def __init__(self, x1, y1):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load("fullhealth.png").convert_alpha()
        shopitems.img.set_colorkey((255, 255 ,255))
        self.images.append(img)
        self.image = self.images[0]
        shopitems.rect = self.image.get_rect()
        shopitems.rect.x = x1
        shopitems.rect.y = y1
