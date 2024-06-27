import pygame
pygame.init()

class health(pygame.sprite.Sprite):       
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        
    def image(self, x, x1, y1):
        img = pygame.image.load(x + "health.png").convert_alpha()
        img.set_colorkey((255, 255 ,255))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    
    def swap_image(self, image):
        img = pygame.image.load(image + "health.png").convert_alpha()
        self.images.append(img)
        self.image = self.images[1]
    
    def swap_back(self):
        self.image = self.images[0]

    def boss_health_image(self, x1, y1):
        img = pygame.image.load("boss_frame.png").convert_alpha()
        img.set_colorkey((255, 255 ,255))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1

    def boss_string_image(self, x1, y1):
        img = pygame.image.load("boss_string.png").convert_alpha()
        img.set_colorkey((255, 255 ,255))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    
    def change_boss_health(self, x):
        x = str(x)
        h1 = pygame.image.load(x + "boss_frame.png")
        self.images.append(h1)
        x = int(x)
        self.image = self.images[x]
    
    def change_boss_health_default(self):
        self.image = self.images[0]