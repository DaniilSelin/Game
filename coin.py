

import pygame
from pygame.sprite import Sprite

class Coin(Sprite):
    
    def __init__(self = None, ai_settings = None, screen = None):
        super(Coin, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = -100
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    
    def update(self):
        self.y += self.ai_settings.speed_coin_factor
        self.rect.y = self.y

    
    def blitme(self, frame_coin):
        self.screen.blit(pygame.image.load('images/Coin/picture (' + str(frame_coin) + ').bmp'), self.rect)

    __classcell__ = None



"""import pygame
from pygame.sprite import Sprite

class Coin(Sprite) :
    #aliens!

    def __init__(self,ai_settings,screen):
        #инициализурем and создаем начальную позицию
        super(Coin,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("images/asteroid.png")
        self.rect = self.image.get_rect()

        # оздаем в 00 потом перемещаем куда надо
        self.rect.x = self.rect.width
        self.rect.y = -100

        #сохранем позицию 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        self.y += self.ai_settings.speed_coin_factor
        self.rect.y = self.y
        
    def blitme(self,frame_coin):
        #ыводим money в текущем полоэении
        self.screen.blit(pygame.image.load('images/Coin/picture ('+str(frame_coin)+').bmp'), self.rect)
"""
