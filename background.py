import pygame

def background(screen,number_bg):
    image = pygame.image.load(f'images/гифка/frame_{number_bg}.bmp')
    screen.blit(image,(0,0))

def menu(screen,number_menu,number_frame):
    image = pygame.image.load(f'images/menu/menu_{number_menu}/frame_{number_frame}.bmp')
    screen.blit(image,(0,0))
    pygame.display.flip()
    
def menu_shop(screen,number_shop):
    
    image_0 = pygame.image.load(f'images/Shop/menu_shop_{number_shop}.png')
    screen.blit(image_0,(0,0))

    with open("Rigth_gamer.txt") as Rigth:
        count_coin = Rigth.readline()
        
    with open('доступ.txt') as file_ds :
        available = file_ds.readline().split()

    if ("toster" in available) == False:
        image_count_coin = pygame.image.load(f'images/Coin/shop_coin.bmp')
        screen.blit(image_count_coin,(400,545))
        screen.blit(pygame.font.SysFont('arial', 12).render("9999",False,(0,0,0)),(440,545))
        
    if ("premium" in available) == False:
        image_count_coin = pygame.image.load(f'images/Coin/shop_coin.bmp')
        screen.blit(image_count_coin,(400,268))
        screen.blit(pygame.font.SysFont('arial', 12).render("25",False,(0,0,0)),(440,268))
    if ("shiza" in available) == False:
        image_count_coin = pygame.image.load(f'images/Coin/shop_coin.bmp')
        screen.blit(image_count_coin,(400,404))
        screen.blit(pygame.font.SysFont('arial', 12).render("100",False,(0,0,0)),(440,404))

    image_count_coin = pygame.image.load(f'images/count_coin.bmp')
    screen.blit(image_count_coin,(0,0))
    screen.blit(pygame.font.SysFont('arial', 36).render(count_coin,False,(50,50,50)),(10,5))
    
    pygame.display.flip()
