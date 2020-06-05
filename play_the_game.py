import pygame
from gamemap import *
from setup import *
from enemy import *
from math import sqrt
from tower import *
from shop import *
from tkinter import Place


def main(): 
    
    #Initialize Game
    pygame.init()
    pygame.display.set_caption('Block Tower Defense ')
    clock = pygame.time.Clock()
    delay = pygame.time.delay(500)
    victory = False
    defeat = False
    
    try:
        #Construct road and initialize gamemap
        
        road = datalist[0]
        
        #Create 10x10 game map
        map = Gamemap(10,10,road)
        #scale road for graphics
        route = map.scale_road()
        
        #road2 = [(0,2),(8,2),(8,5),(2,5),(2,7),(9,7)]
        
        #Positions of road blocks and towers
        occupied =  map.create_route()
        
        #Initialize shop
        cost1 = 50
        cost2 = 150
        cost3 = 200
        cost = None
        ttype = None
        icon1 = Shop(1050, 300, 1)
        icon2 = Shop(1125, 300, 2)
        icon3 = Shop(1200, 300, 3)
        icons = pygame.sprite.Group(icon1,icon2,icon3)
        selectedicons = pygame.sprite.Group(icon1,icon2,icon3)
        
        #Create enemies
        enemywaves = datalist[1]
        totalenemies = enemy_count(enemywaves)
        
        #Helper variables
        enemycount = 0
        
        #Count between waves
        waveframecount = 0
        
        #Count between enemies in a wave
        enemyframecount = 0
        
        #Number of current wave
        wavenumber = 0
         
        type = None
        amount = None
        #Main loops
        done = False
        done1 = False
        quit = False
        #Tower select
        select = None
        selected1 = False
        selected2 = False
        selected3 = False
        range = 0
        
        startimage = pygame.image.load("start1.bmp")
    
    
        while not quit:
            done = False
            pygame.init()
            #Starting loop
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit = True
                        done = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        done = True
                
                if victory:
                    screen.fill(GREEN)
                    
                    font1 = pygame.font.SysFont("None", 150)
                    font2 = pygame.font.SysFont("None", 70)
                    win = font1.render("VICTORY!",1,BLUE_TOWER)
                    score= font2.render("Score: %d"% player.score,1,BLUE_TOWER)
                    again = font2.render("To play again, press R",1,BLUE_TOWER)
                    screen.blit(win,(400,250))
                    screen.blit(score,(475,400))
                    screen.blit(again,(390,600))
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r: 
                        del enemylist[:]
                        del towerlist[:]
                        enemysprites.empty()
                        towersprites.empty()
                        player.money = player.startingmoney
                        player.hp = player.startinghp
                        player.killcount = 0
                        player.score = 0
                        player.wave = 1
                        main()
                
                
                elif defeat:
                    screen.fill(GREEN)
                    
                    font1 = pygame.font.SysFont("None", 150)
                    font2 = pygame.font.SysFont("None", 70)
                    defeat = font1.render("DEFEAT!",1,RED)
                    score= font2.render("Score: %d"% player.score,1,RED)
                    again = font2.render("To play again, press R",1,RED)
                    screen.blit(defeat,(400,250))
                    screen.blit(score,(475,400))
                    screen.blit(again,(390,600))
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r: 
                        del enemylist[:]
                        del towerlist[:]
                        enemysprites.empty()
                        towersprites.empty()
                        player.money = player.startingmoney
                        player.hp = player.startinghp
                        player.killcount = 0
                        player.score = 0
                        player.wave = 1
                        main()
                    
                    
                else:
                    screen.blit(startimage, (0, 0), ((180,270), (1300,1000)))
                pygame.display.flip()
            done = False
            victory = False
            defeat = False
        #Main drawing loop    
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        quit = True
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        done = True
                        quit = True
                    
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r: 
                            del enemylist[:]
                            del towerlist[:]
                            enemysprites.empty()
                            towersprites.empty()
                            player.money = player.startingmoney
                            player.health = player.startinghp
                            player.killcount = 0
                            player.score = 0
                            player.wave = 1
                            main()
                         
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        
                        mousex,mousey = pygame.mouse.get_pos()
                        #Choose tower from shop
                        if icon1.rect.collidepoint(pygame.mouse.get_pos()):            
                            ttype = 1
                            cost = cost1
                            range = 200
                            selected1 = True
                            selected2 = False
                            selected3 = False
                        elif icon2.rect.collidepoint(pygame.mouse.get_pos()):
                            ttype = 2
                            cost = cost2
                            range = 300
                            selected1 = False
                            selected2 = True
                            selected3 = False
                        elif icon3.rect.collidepoint(pygame.mouse.get_pos()):
                            ttype = 3
                            cost = cost3
                            range = 700
                            selected1 = False
                            selected2 = False
                            selected3 = True
                        
                        
                        #Add tower to map
                        if (mousex < 1000 and mousey < 1000):
                            pos = int(mousex/100),int(mousey/100)
                            #Check if the position is free
                            if pos not in occupied: 
                                    if ttype is not None and cost is not None:
                                        if player.money >= cost:
                                            occupied.append(pos)
                                            Tower(pos[0]*100+18,pos[1]*100+18,ttype)
                                            player.money -= cost
                                            selected1 = False
                                            selected2 = False
                                            selected3 = False
                                            
                    #Upgrade tower
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                        
                        for tower in towerlist:
                            if tower.rect.collidepoint(pygame.mouse.get_pos()):
                                
                                if tower.upgrade <= player.money:
                                    player.money -= tower.upgrade
                                    tower.up()
                                
                #Fill screen background       
                screen.fill(GREEN)
                
                #Draw road
                map.draw_road(road)
                
                #Tower selection graphics
                if selected1:
                    mousex,mousey = pygame.mouse.get_pos()
                    
                    if (mousex < 1000 and mousey < 1000):
                            pos = int(mousex/100),int(mousey/100)
                            pygame.draw.rect(screen, BLUE_TOWER, [pos[0]*100, pos[1]*100, 100, 100], 3)
                            pygame.draw.circle(screen,BLUE_TOWER,(mousex,mousey),range,3)
                    screen.blit(icon1.image,(mousex-20,mousey-20))    
                    
                if selected2:
                    mousex,mousey = pygame.mouse.get_pos()
                    if (mousex < 1000 and mousey < 1000):
                            pos = int(mousex/100),int(mousey/100)
                            pygame.draw.rect(screen, RED_TOWER, [pos[0]*100, pos[1]*100, 100, 100], 3)
                            pygame.draw.circle(screen,RED_TOWER,(mousex,mousey),range,3)
                    screen.blit(icon2.image,(mousex-20,mousey-20))
                
                if selected3:
                    mousex,mousey = pygame.mouse.get_pos()
                    if (mousex < 1000 and mousey < 1000):
                            pos = int(mousex/100),int(mousey/100)
                            pygame.draw.rect(screen, YELLOW_TOWER, [pos[0]*100, pos[1]*100, 100, 100], 3)
                            pygame.draw.circle(screen,YELLOW_TOWER,(mousex,mousey),range-200,3)
                    screen.blit(icon3.image,(mousex-20,mousey-20))
                
                #Read enemywaves data
                if wavenumber < waves:
                    data = enemywaves[wavenumber]
                    type = data[0]
                    amount = data[1]         
                
                #Add enemies in spesific wave
                if enemyframecount > 60 and enemycount < amount:
                    enemy = Enemy(wavenumber,route,type)
                    enemycount += 1
                    if route[0][0]==0:
                        enemy.rect.y = route[0][1]
                        enemy.rect.x = -75
                    if type == 3:
                        enemyframecount = -60 
                        
                    else:
                        enemyframecount = 0
                        
                
                #Cooldown between waves
                if waveframecount > amount*100:
                    wavenumber += 1
                    waveframecount = 0
                    player.wave += 1
                    enemycount = 0
                
                waveframecount += 1
                enemyframecount += 1
                
                #Calls update() for sprites  
                enemysprites.update()
                towersprites.update()
                icons.update()
                selectedicons.update()
                
                #Draw towers
                towersprites.draw(screen)
                icons.draw(screen)
                
                #Tower shooting
                for tower in towerlist:  
                    enemytarget = tower.target()
                    if enemytarget != None:
                        if len(enemylist)==1 and enemycount==1:
                            tower.cdcounter =tower.cooldown-1
                            
                        if(tower.cdcounter>tower.cooldown):
                            if tower.shots<3:
                                pygame.draw.line(screen,tower.color,[tower.rect.x+25,tower.rect.y+25],[enemytarget[0]+25,enemytarget[1]+25],3)
                                tower.shots += 1
                                tower.isShooting = True
                            else:
                                tower.isShooting = False
                                tower.cdcounter = 0
                                tower.shots = 0
                        tower.cdcounter += 1
                
                #Enemy hp bars  
                for enemy in enemylist:
                    if(enemy.hp > 0):
                        pygame.draw.line(screen, (255,0,0), (enemy.rect.left-5,enemy.rect.top-5),(enemy.rect.right,enemy.rect.top-5), 5)   
                        pygame.draw.line(screen, GREEN2, (enemy.rect.left-5,enemy.rect.top-5),(enemy.rect.left+(enemy.hp*1.0/enemy.basehp*1.0)*enemy.rect.width,enemy.rect.top-5), 5)
                
                #Draw enemies
                enemysprites.draw(screen)
                
                #Show game information
                show_game_info()    
                
                #Limit to 60 frames per second
                clock.tick(60)
                
                #Victory
                if wavenumber == waves-1 and player.killcount==totalenemies:
                    victory = True
                    done = True
                
                #Defeat
                if player.hp <= 0:
                    defeat = True
                    done = True
      
             
                pygame.display.flip()
                
             
        pygame.quit()
        sys.exit()
    #handles error in datafile
    except TypeError:
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                    done = True
            screen.fill(RED)
            font1 = pygame.font.SysFont("None", 70)
            error = font1.render("Could not open datafile. Please give correct file :)",1,BLACK)
            screen.blit(error,(100,350))
            pygame.display.flip()               
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    main()