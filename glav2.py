import pygame
import winsound
import sys
from timer import Timer
from setting import Setting
from background import *
from ship import *
from asteroid import Asteroid
from coin import Coin
import game_functions as gf
from pygame.sprite import Group

"""Слишком жирный модуль"""

def glav_game():
    #инициализирует игру и создает обьект экрана.
    pygame.init()
    #для настроект срздал отдельный класс
    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
        )
    pygame.display.set_caption("Asteroid hit!")
    run_menu(screen,ai_settings)
    
def run_menu(screen,ai_settings):
    #ход меню
    number_menu = 4
    number_frame = 0
    #основной цикл меню
    while True :
        #функция для отображения меню
        menu(screen,number_menu,int(number_frame))
        #ход меню
        if number_frame>= 21.9 :
            number_frame = 0
        number_frame +=0.007
        #проверка всех нажатий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #перемещение по меню
                if event.key == pygame.K_RETURN:
                    winsound.PlaySound('menu_ENTER.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                    if number_menu == 4 :
                        run_game(screen,ai_settings)
                        break
                    elif number_menu == 3 :
                         run_shop(screen,ai_settings)
                    elif number_menu == 1 :
                        sys.exit()
                elif event.key == pygame.K_UP :
                    winsound.PlaySound('menu_change.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                    if number_menu == 4 :
                        number_menu = 1
                    else :
                        number_menu += 1
                elif event.key == pygame.K_DOWN :
                    winsound.PlaySound('menu_change.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                    if number_menu == 1 :
                        number_menu = 4
                    else :
                        number_menu -= 1
                        
def run_shop(screen,ai_settings):
    number_shop = 1
    #основной цикл shop
    while True :
        menu_shop(screen,number_shop)

        with open('доступ.txt') as file_ds :
                        available = file_ds.readline().split()

        #проверка всех нажатий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN  :
                    winsound.PlaySound('menu_ENTER.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                        
                    if number_shop == 2 :
                        run_menu(screen,ai_settings)
                        break
                    
                    elif number_shop == 3:
                        #сначала проверяем куплено ли, а потом смотрим хватает ли денек
                        if "toster" in available:
                            with open('name_ship.txt',"w") as name_ship :
                                name_ship.write("toster.png")
                        else :
                            lvl_up = ""
                            with open('rigth_gamer.txt') as Rigth :
                                count_coin = int(Rigth.readline())
                            if count_coin>=9999 :
                                winsound.PlaySound('pay.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                                for item in available :
                                    lvl_up += item + " "
                                with open('доступ.txt',"w") as file_ds : 
                                    file_ds.write("toster "+lvl_up)
                                with open('rigth_gamer.txt',"w") as Rigth :
                                    Rigth.write(str(count_coin-9999))
                            else :
                                winsound.PlaySound('not_pay.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                                    
                    elif number_shop == 4 :
                        if "shiza" in available:
                            with open('name_ship.txt',"w") as name_ship :
                                name_ship.write("Шиза.bmp")
                        else :
                            lvl_up = ""
                            with open('rigth_gamer.txt') as Rigth :
                                count_coin = int(Rigth.readline())
                            if count_coin>=100 :
                                winsound.PlaySound('pay.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                                for item in available :
                                    lvl_up += item + " "
                                with open('доступ.txt',"w") as file_ds : 
                                    file_ds.write("shiza "+lvl_up)
                                with open('rigth_gamer.txt',"w") as Rigth :
                                    Rigth.write(str(count_coin-100))
                            else :
                                winsound.PlaySound('not_pay.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                                
                    elif number_shop == 5 :
                        if "premium" in available:
                            with open('name_ship.txt',"w") as name_ship :
                                name_ship.write("ship_premium.png")
                        else :
                            lvl_up = ""
                            with open('rigth_gamer.txt') as Rigth :
                                count_coin = int(Rigth.readline())
                            if count_coin>=25 :
                                winsound.PlaySound('pay.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                                for item in available :
                                    lvl_up += item + " "
                                with open('доступ.txt',"w") as file_ds : 
                                    file_ds.write("premium "+lvl_up)
                                with open('rigth_gamer.txt',"w") as Rigth :
                                    Rigth.write(str(count_coin-25))
                            else :
                                winsound.PlaySound('not_pay.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)

                                    
                    elif number_shop == 1 :
                        with open('name_ship.txt',"w") as name_ship :
                            name_ship.write("ship_base.png")
                            
                elif event.key == pygame.K_UP :
                    winsound.PlaySound('menu_change.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                    if number_shop == 5 :
                        number_shop = 1
                    else :
                        number_shop += 1
                elif event.key == pygame.K_DOWN :
                    winsound.PlaySound('menu_change.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                    if number_shop == 1 :
                        number_shop = 5
                    else :
                        number_shop -= 1


def game_over_st(ai_settings, screen, boom, asteroids, coins, bullets, number_bg, frame_asteroid, frame_coin, count_coin):
    #решил не мучатся и написать для взрыва отдельный ход
    frame_boom = 0
    while frame_boom < 27:

        if number_bg >= 15:
            number_bg = 1
        number_bg += 0.05
        if frame_asteroid >= 7:
            frame_asteroid = 1
        frame_asteroid += 0.05
        if frame_coin >= 7:
            frame_coin = 1
        frame_coin += 0.05

        screen.fill(ai_settings.bg_color)
        background(screen, int(number_bg))
        #поверки нафиш не нужны, тэ кэк все локальные автоматом подчистяца
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        collisions = pygame.sprite.groupcollide(bullets, asteroids, True, True)
        for asteroid in asteroids:
            asteroid.blitme()
            asteroid.update()
        for coin in coins:
            coin.blitme(int(frame_coin))
        image_count_coin = pygame.image.load('images/count_coin.bmp')

        boom.blitme(int(frame_boom))
        frame_boom+=0.3
        screen.blit(image_count_coin, (0, 0))
        screen.blit(pygame.font.SysFont('arial', 36).render(str(count_coin), False, (50, 50, 50)), (10, 5))
        pygame.display.flip()

def run_game(screen,ai_settings):
    with open('rigth_gamer.txt') as Rigth :
        count_coin = int(Rigth.readline())
    #ход фона
    number_bg = 1
    frame_asteroid = 1
    frame_coin = 1
    frame_boom = 1
    #создание корабля
    ship = Ship(ai_settings,screen)
    asteroid = Asteroid(ai_settings,screen)
    
    #создание группы для пуфыль
    bullets = Group()
    asteroids = Group()
    coins = Group()
    timer_created_asteroid = Timer()
    timer_created_coin = Timer()
    timer_created_coin.timer_start()
    timer_created_asteroid.timer_start()
    #запуск основного цикла игры
    while True :
            
        #создаем астероиды по таймингу :
        if timer_created_asteroid.timer_stop() > 0.2*10**9 :
            gf.create_fleet(ai_settings,screen,asteroids)
            timer_created_asteroid.timer_start()
        #создаем монетки по таймингу
        if timer_created_coin.timer_stop() > 5*10**9 :
            gf.create_coin(ai_settings,screen,coins)
            timer_created_coin.timer_start()
            
        if number_bg >= 15:
            number_bg = 1
        number_bg += 0.05

        #тэк кэк у этого класса есть свойство frame
        for asteroid in asteroids:
            asteroid.frame+=0.05

        if frame_coin >= 7:
            frame_coin = 1
        frame_coin += 0.05

        #чекаем события, и все обноволяем
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        asteroids.update()
        coins.update()
        bullets.update()
        for coin in coins:
            #переписать!
            if pygame.sprite.spritecollideany(ship, coins):
                winsound.PlaySound('coin_soundt.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                coins.remove(coin)
                count_coin +=1
                with open('rigth_gamer.txt',"w") as Rigth:
                    Rigth.write(str(count_coin))
        if gf.update_screen(ai_settings,screen,ship,asteroids,coins,bullets,int(number_bg),int(frame_asteroid),int(frame_coin),count_coin) == 11:
            #при уничтожениии кораблика мутим анимацию взрыва
            winsound.PlaySound('boom.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            boom = Boom(screen,ship.centerx,ship.centery)
            game_over_st(ai_settings,screen,boom,asteroids,coins,bullets,number_bg,frame_asteroid,frame_coin,count_coin)
            run_menu(screen,ai_settings)

glav_game()

