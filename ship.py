
import pygame
class Boom():
    #бредовый класс для взрыва
    def __init__(self,screen,centerx_ship,centery_ship):
        self.screen = screen
        # Загруза первого фрейма взрыва и выделение области
        self.image = pygame.image.load(f'images/Boom/frame_0_delay-0.1s.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # сразу перекидываем на нужные координаты
        self.rect.centerx = centerx_ship
        self.rect.centery = centery_ship

    def blitme(self, frame_boom):
        self.screen.blit(pygame.image.load(f'images/Boom/frame_{frame_boom}_delay-0.1s.gif'), self.rect)

class Ship():
    def __init__(self,ai_settings,screen):
        #инициализируем корабль и ставим его в начальное положение
        self.screen = screen
        self.ai_settings = ai_settings

        #Загрущка изображение корабля и получение прямоугольника
        with open('name_ship.txt') as name_ship:
            name_ship_png = name_ship.readline()
            self.image = pygame.image.load(f'images/Ships/{name_ship_png}')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #каждый клоабль появляется в низу экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right - 15:
            self.centerx += self.ai_settings.speed_ship_factor
        if self.moving_left and self.rect.left > self.screen_rect.left + 15 :
            self.centerx -= self.ai_settings.speed_ship_factor
        if self.moving_top and self.rect.top > self.screen_rect.top + 15 :
            self.centery -= self.ai_settings.speed_ship_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom - 15 :
            self.centery += self.ai_settings.speed_ship_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def blitme(self):
        #рисуем корабль в текущей позиии
        self.screen.blit(self.image,self.rect)

