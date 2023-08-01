
import sys
from background import background
from timer import Timer
import pygame
import winsound
import ship
import random
from bullet import Bullet
from asteroid import Asteroid
from coin import Coin

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_d:
        ship.moving_right = True
    if event.key == pygame.K_a:
        ship.moving_left = True
    if event.key == pygame.K_w:
        ship.moving_top = True
    if event.key == pygame.K_s:
        ship.moving_bottom = True
    if event.key == pygame.K_SPACE and len(bullets) < 3:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        winsound.PlaySound('bulletGo.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)


def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_w:
        ship.moving_top = False
    if event.key == pygame.K_s:
        ship.moving_bottom = False



def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_bullets(bullets):
    for bullet in bullets:
        if bullet.y < 0:
            bullets.remove(bullet)


def check_coin(coins):
    for coin in coins:
        if coin.y > 700:
            coins.remove(coin)


def check_asteroid(asteroids):
    for asteroid in asteroids:
        if asteroid.y > 700:
            asteroids.remove(asteroid)


def create_fleet(ai_settings, screen, asteroids):
    asteroid = Asteroid(ai_settings, screen)
    asteroid_width = asteroid.rect.width
    asteroid.rect.x = random.randint(10, ai_settings.screen_width - 30)
    asteroids.add(asteroid)


def create_coin(ai_settings, screen, coins):
    coin = Coin(ai_settings, screen)
    coin_width = coin.rect.width
    coin.rect.x = random.randint(10, ai_settings.screen_width - 30)
    coins.add(coin)


def update_screen(ai_settings, screen, ship, asteroids, coins, bullets, number_bg, frame_asteroid, frame_coin, count_coin):
    screen.fill(ai_settings.bg_color)
    background(screen, number_bg)
    check_bullets(bullets)
    check_asteroid(asteroids)
    check_coin(coins)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    collisions = pygame.sprite.groupcollide(bullets, asteroids, True, True)
    if pygame.sprite.spritecollideany(ship, asteroids):
        for asteroid in asteroids:
            if ship.rect.colliderect(asteroid.rect):
                asteroids.remove(asteroid)
        return 11
    for asteroid in asteroids:
        asteroid.frame += 0.05
        asteroid.blitme()
    for coin in coins:
        coin.blitme(frame_coin)
    image_count_coin = pygame.image.load('images/count_coin.bmp')
    ship.blitme()
    screen.blit(image_count_coin, (0, 0))
    screen.blit(pygame.font.SysFont('arial', 36).render(str(count_coin), False, (50, 50, 50)), (10, 5))
    pygame.display.flip()