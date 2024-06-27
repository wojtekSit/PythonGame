from audioop import cross
from re import A, X
from this import d
import pygame
from pygame import sprite
from pygame.constants import KEYDOWN
import random
import time
from Sprite import Player
from Enemy import enemy
from pygame.locals import *
from gates import gate
from projectiles import projectile
import math
from health import health
from damageflash import damageflash
from shopitems import shopitems
from Boss import boss

#setup
# shop_list = pygame.sprite.Group()
# hapeki = shopitems(500, 500)
# hapeki.add(shop_list)
pygame.init()
pygame.display.set_caption("rougelike")
pygame.mouse.set_visible(False)
pygame.font.init()
timer = 0
worldx = 1000
worldy = 1000
fps = 60
font = pygame.font.SysFont("Arial", 18)
clock = pygame.time.Clock()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load("background0.png")
backdropbox = world.get_rect()
screen_rect = pygame.Rect((0, 0), (worldx, worldy))
coin = pygame.image.load("coin.png").convert_alpha()
flash1 = damageflash(0, 0)
screen_flash_group = pygame.sprite.Group()
flash1.add(screen_flash_group)
attackspeeditem = pygame.image.load("crossbow.png").convert_alpha()
healthrestore = pygame.image.load("fullhealth.png").convert_alpha()
crossshooting = pygame.image.load("cross.png").convert_alpha()
#player

player = Player(500, 500)       #spawning player at coordinates
player_list = pygame.sprite.Group()
player_list.add(player)

#enemies

enemies_list = pygame.sprite.Group()
def spawn_enemies():
    global level
    how_many_enemies = level*random.randrange(1,5)
    for i in range(how_many_enemies):
        z = random_of_ranges()
        if z == 1:
            x = random.randrange(100,250)
            y = random.randrange(100,950)
            enemy1 = enemy(x, y)
            enemies_list.add(enemy1)
        if z == 2:
            x = random.randrange(800,950)
            y = random.randrange(100,950)
            enemy1 = enemy(x, y)
            enemies_list.add(enemy1)
        if z == 3:
            x = random.randrange(100,950)
            y = random.randrange(100,250)
            enemy1 = enemy(x, y)
            enemies_list.add(enemy1)
        if z == 4:
            x = random.randrange(100,950)
            y = random.randrange(800,950)
            enemy1 = enemy(x, y)
            enemies_list.add(enemy1)        
def random_of_ranges():
    x = random.randrange(1,5)
    return x 
#boss

boss_list = pygame.sprite.Group()

def boss_spawning():
    global n, boss1, level
    if level%3 == 0:
        z = random.randrange(1,5)
        if z == 1:
            boss1 = boss(10,10)
        elif z == 2:
            boss1 = boss(13,829)
        elif z == 3:
            boss1 = boss(829,826)
        elif z == 4:
            boss1 = boss(826,10)
        boss_list.add(boss1)
        return boss1.rect.x, boss1.rect.y

def boss_player_collision():
    if pygame.sprite.spritecollide(player, boss_list, False, False):
        for i in boss_list:
            if i.rect.x < player.rect.x and i.rect.y < player.rect.y:
                player.rect.x += 75
                player.rect.y += 75
            if i.rect.x > player.rect.x and i.rect.y < player.rect.y:
                player.rect.x -= 75
                player.rect.y += 75 
            if i.rect.x < player.rect.x and i.rect.y > player.rect.y:
                player.rect.x += 75
                player.rect.y -= 75
            if i.rect.x > player.rect.x and i.rect.y > player.rect.y:
                player.rect.x -= 75
                player.rect.y -= 75
            if i.rect.x == player.rect.x and i.rect.y < player.rect.y:
                player.rect.x += 0
                player.rect.y += 75
            if i.rect.x == player.rect.x and i.rect.y > player.rect.y:
                player.rect.x += 0
                player.rect.y -= 75
            if i.rect.x < player.rect.x and i.rect.y == player.rect.y:
                player.rect.x += 75
                player.rect.y += 0
            if i.rect.x > player.rect.x and i.rect.y == player.rect.y:
                player.rect.x -= 75
                player.rect.y -= 0 
        global lifes
        lifes -= 1

def boss_spawning_bullets(bossvar):
    boss_strzal = projectile(bossvar)
    bullets_list.add(boss_strzal)
    boss_strzal.boss_shooting(bossvar)

#gates

gate_list = pygame.sprite.Group()
gate1 = gate(500, 0)
gate2 = gate(0, 500)
gate3 = gate(500, 934)
gate4 = gate(940, 500)
gate_list.add(gate1)
gate_list.add(gate2)
gate_list.add(gate3)
gate_list.add(gate4)

#spawning bullets for player
bullets_list = pygame.sprite.Group()
cross_shooting_list = pygame.sprite.Group()
def spawning_bullets(key):
    global crosshooter
    if crossshooter == False:
        pewpew = projectile(player.rect.x+21, player.rect.y+21)
        bullets_list.add(pewpew)
        pewpew.shooting(key)
    if (money >= 15):
        '''pewpew.upgraded_bullets()'''
    if crossshooter == True:
        pewpew1 = projectile(player.rect.x+21, player.rect.y+21)
        pewpew2 = projectile(player.rect.x+21, player.rect.y+21)
        pewpew3 = projectile(player.rect.x+21, player.rect.y+21)
        pewpew4 = projectile(player.rect.x+21, player.rect.y+21)
        cross_shooting_list.add(pewpew1,pewpew2,pewpew3,pewpew4)
        pewpew1.cross_shooting1(key)
        pewpew2.cross_shooting2(key)
        pewpew3.cross_shooting3(key)
        pewpew4.cross_shooting4(key)

#displaying fps in upper left corner
def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

#displaying money (just the number)
def display_money():
    global money
    moneytext = font.render(str(money), 1, pygame.Color("coral"))
    return moneytext

def map_change():
    global backdrop
    global mapnumber
    global variety
    variety = mapnumber
    mapnumber = str(random.randint(0,4))
    if(variety != mapnumber ):
        backdrop = pygame.image.load("background" + mapnumber + ".png")
    else:
        map_change()



def enemy_player_collision():
    if pygame.sprite.spritecollide(player, enemies_list, False, False):
            for i in enemies_list:
                if i.rect.x > player.rect.x and i.rect.y > player.rect.y:
                    i.rect.x += 75
                    i.rect.y += 75
                if i.rect.x < player.rect.x and i.rect.y > player.rect.y:
                    i.rect.x -= 75
                    i.rect.y += 75 
                if i.rect.x > player.rect.x and i.rect.y < player.rect.y:
                    i.rect.x += 75
                    i.rect.y -= 75
                if i.rect.x < player.rect.x and i.rect.y < player.rect.y:
                    i.rect.x -= 75
                    i.rect.y -= 75
                if i.rect.x == player.rect.x and i.rect.y > player.rect.y:
                    i.rect.x += 0
                    i.rect.y += 75
                if i.rect.x == player.rect.x and i.rect.y < player.rect.y:
                    i.rect.x += 0
                    i.rect.y -= 75    
                if i.rect.x > player.rect.x and i.rect.y == player.rect.y:
                    i.rect.x += 75
                    i.rect.y += 0
                if i.rect.x < player.rect.x and i.rect.y == player.rect.y:
                    i.rect.x -= 75
                    i.rect.y -= 0 
            global lifes
            lifes -= 1

health_list = pygame.sprite.Group()   
q = "full"
hp1 = health()
hp1.image(q, 700, 20)
hp2 = health()
hp2.image(q, 730, 20)    
hp3 = health()
hp3.image(q, 760, 20)
hp4 = health()
hp4.image(q, 790, 20)
hp5 = health()
hp5.image(q, 820, 20)      
health_list.add(hp1, hp2, hp3, hp4, hp5)

boss_health_list = pygame.sprite.Group()
bosshp = health()
bosshp.boss_health_image(750,950)
boss_string = health()
boss_string.boss_string_image(735,920)
boss_health_list.add(bosshp, boss_string)

#main

def main():
    
    global variety, mapnumber, lifes, money, level, bossvar, n, d, crossshooter
    d = 1
    n = 1
    bossvar = 0
    mapnumber = 0
    lifes = 5
    cooldown_tracker = 0
    money = 100
    level = 2
    attackspeed = 400
    boss_health_points = 1
    crossshooter = False
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not enemies_list and not boss_list:  
            if pygame.sprite.spritecollide(player, gate_list, True): 
                gate1 = gate(500, 0)
                gate2 = gate(0, 500)
                gate3 = gate(500, 934)
                gate4 = gate(940, 500)
                gate_list.add(gate1)
                gate_list.add(gate2)
                gate_list.add(gate3)
                gate_list.add(gate4)
                map_change()
                player.rect.x = 500
                player.rect.y = 500
                level += 1
                n += 1
                if mapnumber != "1":
                    spawn_enemies()
                    bossvar = boss_spawning()

        if pygame.sprite.groupcollide(bullets_list, enemies_list, True, True):
            money += 1
            
        if pygame.sprite.groupcollide(cross_shooting_list, enemies_list, True, True):
            money += 1
            
        #cooldown on shooting
        cooldown_tracker += 10
        if cooldown_tracker > attackspeed:
            if event.type == pygame.KEYDOWN:
                spawning_bullets(event.key)
                cooldown_tracker = 0
        
        
        #game stops at 0 lifes
        if lifes == 0:
            running = False
        
        if pygame.sprite.spritecollide(player, enemies_list, False, False):
            if lifes == 5:
                hp5.swap_image("empty")
            if lifes == 4:
                hp4.swap_image("empty")
            if lifes == 3:
                hp3.swap_image("empty")  
            if lifes == 2:
                hp2.swap_image("empty")

        if pygame.sprite.spritecollide(player, boss_list, False, False):
            if lifes == 5:
                hp5.swap_image("empty")
            if lifes == 4:
                hp4.swap_image("empty")
            if lifes == 3:
                hp3.swap_image("empty")  
            if lifes == 2:
                hp2.swap_image("empty")
        enemy_player_collision()
        # if level == 3*n:
        #     boss_spawning_bullets(bossvar)
            
        boss_player_collision()
        player.moving()
        for i in enemies_list:
            i.following()
        for i in boss_list:
            i.following()
        world.blit(backdrop, backdropbox) #draws backdrop file background onto the backdropbox (game rect)
        if pygame.sprite.spritecollide(player, enemies_list, False, False):
            screen_flash_group.draw(world)
        player_list.draw(world)
        enemies_list.draw(world)
        if boss_health_points < 15:
            boss_list.draw(world)
        if boss_health_points == 15:
            boss_list.remove(boss1)
            bosshp.change_boss_health_default()
            boss_health_points = 1
        if crossshooter == True:
            cross_shooting_list.draw(world)
            cross_shooting_list.update()
        else:
            bullets_list.draw(world)
            bullets_list.update()
        health_list.draw(world)
        if level%3 == 0:
            boss_health_list.draw(world)
        if pygame.sprite.groupcollide(bullets_list, boss_list, True, False):
            bosshp.change_boss_health(boss_health_points)
            boss_health_points += 1
        if pygame.sprite.groupcollide(cross_shooting_list, boss_list, True, False):
            bosshp.change_boss_health(boss_health_points)
            boss_health_points += 1 
        world.blit(coin, (700, 45))
        world.blit(display_money(), (735,45))
        world.blit(update_fps(), (10,0))
        if not enemies_list and not boss_list:
            gate_list.draw(world)
        #shop attack speed increase
        if money >= 10 and mapnumber == "1":
            world.blit(attackspeeditem, (50, 50))
            if player.rect.x == 50 and player.rect.y == 50:
                attackspeed -= 400
                money -= 10

        #shop cross shooting
        if money >= 15 and mapnumber == "1" and crossshooter == False:
            world.blit(crossshooting, (250, 250))
            if player.rect.x == 250 and player.rect.y == 250:
                money -=15
                crossshooter = True
        #shop life restore
        if money >= 5 and mapnumber == "1":   
            world.blit(healthrestore, (900, 900))
            if player.rect.x == 900 and player.rect.y == 900:
                if lifes == 4:
                    money -= 5
                    lifes += 1
                    hp5.swap_back()
                if lifes == 3:
                    money -=5
                    lifes += 1
                    hp4.swap_back()
                if lifes == 2:
                    money -= 5
                    lifes += 1
                    hp3.swap_back() 
                if lifes == 1:
                    money -=5
                    lifes += 1
                    hp2.swap_back()
        pygame.display.flip()
        clock.tick(fps)
        
main()
