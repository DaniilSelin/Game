
import pygame
from pygame.sprite import Sprite

class Asteroid(Sprite):
    
    def __init__(self = None, ai_settings = None, screen = None):
        super(Asteroid, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #для анимации
        self.frame = 1
        self.image = pygame.image.load('images/asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = -100
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    
    def update(self):
        #обновление позиции
        self.y += self.ai_settings.speed_asteroid_factor
        self.rect.y = self.y

    
    def blitme(self):
        if self.frame > 7:
            self.frame = 1
        self.screen.blit(pygame.image.load(f'images/Астероид/picture ({int(self.frame)}).bmp'), self.rect)