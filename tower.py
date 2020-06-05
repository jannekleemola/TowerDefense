import pygame,os
from setup import *
from math import sqrt


class Tower(pygame.sprite.Sprite):   
    def __init__(self,x,y,type):
        #Initialize
        super().__init__()
        towerlist.append(self)
        towersprites.add(self)
        
        self.type = type
        self.level = 1
        
        if self.type == 1:
            #Image
            self.image = pygame.Surface([60, 60])
            self.color = BLUE_TOWER
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            #Parameters
            self.damage = 10
            self.cost = 100
            self.range = 200
            self.cooldown = 60
            self.upgrade = 150
            #Helper variables
            self.cdcounter = 0
            self.shots = 0
        
        if self.type == 2:    
            self.image = pygame.Surface([60, 60])
            self.color = RED_TOWER
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            #Parameters
            self.damage = 20
            self.cost = 150
            self.range = 300
            self.cooldown = 80
            self.upgrade = 200
            #Helper variables
            self.cdcounter = 0
            self.shots = 0
        
        if self.type == 3:
            self.image = pygame.Surface([60, 60])
            self.color = YELLOW_TOWER
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            #Parameters
            self.damage = 1
            self.cost = 200
            self.range = 500
            self.cooldown = 0
            self.upgrade = 300
            #Helper variables
            self.cdcounter = 0
            self.shots = 0
        
        self.rect.x = x
        self.rect.y = y
        
        self.isShooting = False
  
    #Returns towers target coordinates
    def target(self):
        for enemy in enemylist:       
            distance = sqrt((self.rect.x - enemy.rect.x)**2+(self.rect.y-enemy.rect.y)**2)
            if distance < self.range:
                if self.isShooting and self.shots==2:
                    enemy.hp -= self.damage
                return enemy.rect.x,enemy.rect.y
    
    #Upgrade tower    
    def up(self):
        if self.level == 1:
            self.level = 2
            
            if self.type == 1:
                self.color = BLUE_TOWER2
                self.image.fill(self.color)
                self.damage = 15
                self.range = 225
                self.cooldown = 55
                self.upgrade = 200
        
            if self.type == 2:
                self.color = RED_TOWER2
                self.image.fill(self.color)
                self.damage = 30
                self.range = 325
                self.cooldown = 75
                self.upgrade = 300
            
            if self.type == 3:
                self.color = YELLOW_TOWER2
                self.image.fill(self.color)
                self.damage = 2
                self.range = 525
                self.cooldown = 0
                self.upgrade = 500
            return
        
        if self.level == 2:
            self.level = 3  
            
            if self.type == 1:
                self.color = BLUE_TOWER3
                self.image.fill(self.color)
                self.damage = 25
                self.range = 250
                self.cooldown = 50
                
            if self.type == 2:
                self.color = RED_TOWER3
                self.image.fill(self.color)
                self.damage = 40
                self.range = 350
                self.cooldown = 70
                
            if self.type == 3:
                self.color = YELLOW_TOWER3
                self.image.fill(self.color)
                self.damage = 5
                self.range = 550
                self.cooldown = 0
            return   
    #Show tower info
    def tower_info(self):
        self.Font = pygame.font.SysFont("None", 30)
        self.Font2 = pygame.font.SysFont("None", 40)
        self.Font3 = pygame.font.SysFont("None", 50)
        
        damage = self.Font.render("Damage: %d"% self.damage,1,self.color)
        upcost = self.Font.render("Upgrade cost: %d"% self.upgrade,1, self.color)
        range = self.Font.render("Range: %d"% self.range,1, self.color)
        cooldown = self.Font.render("Cooldown: %1.1f"% self.cooldown,1, self.color)
        maxed = self.Font3.render("MAXED OUT",1,self.color)
        
       
        x = 1030
        y = 300+100
        
        if self.level < 3:
            
            screen.blit(upcost,(x,y))
            screen.blit(damage,(x,y+50))
            screen.blit(range,(x,y+25))
            screen.blit(cooldown,(x,y+75))
            
        else:    
            screen.blit(damage,(x,y))
            screen.blit(range,(x,y+25))
            screen.blit(cooldown,(x,y+50))
            screen.blit(maxed,(x,y+80))
    
    
    #Update tower
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.tower_info()
            pygame.draw.circle(screen,self.color,self.rect.center,self.range,3)



       
        