import pygame,os
from setup import *
from math import sqrt

class Shop(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)
        
        self.type = type
        #Blue tower
        if self.type == 1:
            self.image = pygame.Surface([40, 40])
            self.color = BLUE_TOWER
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            #Parameters
            self.damage = 10
            self.cost = 100
            self.range = 200
            self.cooldown = 60
        #Red tower
        if self.type == 2:    
            self.image = pygame.Surface([40, 40])
            self.color = RED_TOWER
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            #Parameters
            self.damage = 20
            self.cost = 150
            self.range = 300
            self.cooldown = 80
        #Yellow tower
        if self.type == 3:
            self.image = pygame.Surface([40, 40])
            self.color = YELLOW_TOWER
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            #Parameters
            self.damage = 1
            self.cost = 200
            self.range = 500
            self.cooldown = 0
        
        self.rect.x = x
        self.rect.y = y
        self.Font = pygame.font.SysFont("None", 30)
        self.Font2 = pygame.font.SysFont("None", 40)
        
    #Update shop
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.shop_info()
            pygame.draw.rect(screen, self.color, [ self.rect.x-5,self.rect.y-5, 50, 50], 3)
    
    #Show shop info    
    def shop_info(self):
        damage = self.Font.render("Damage: %d"% self.damage,1,self.color)
        cost = self.Font.render("Cost: %d"% self.cost,1, self.color)
        range = self.Font.render("Range: %d"% self.range,1, self.color)
        cooldown = self.Font.render("Cooldown: %1.1f"% self.cooldown,1, self.color)
        shop = self.Font2.render("Kill them all!",1, self.color)
       
        x = 1030
        y = 300+100

        screen.blit(cost,(x,y))
        screen.blit(damage,(x,y+50))
        screen.blit(range,(x,y+25))
        screen.blit(cooldown,(x,y+75))
        screen.blit(shop,(x,y+200))