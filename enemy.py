import pygame, os
from setup import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self, wave,route,type):
        #Initialize
        super().__init__()
        enemylist.append(self)
        enemysprites.add(self)
        
        self.route = route
        self.type = type
        
        if type == 1:
            #Image
            self.image = pygame.Surface([50, 50])
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            #Parameters
            if wave > 3:
                self.hp =40+2*wave*wave
                self.basehp = self.hp
                self.score = 100+5*wave
                self.bounty = 25+2*wave
            else:
                self.hp =30+2*wave
                self.basehp = self.hp
                self.score = 100
                self.bounty = 25
            
            self.speed = 2
        
        if type == 2:
            #Image
            self.image = pygame.Surface([50, 50])
            self.image.fill(INDIGO)
            self.rect = self.image.get_rect()
            #Parameters
            if wave > 3:
                self.hp =70+3*wave*wave
                self.basehp = self.hp
                self.score = 110+5*wave
                self.bounty = 30+2*wave
            else:
                self.hp =40+2*wave
                self.basehp = self.hp
                self.score = 110
                self.bounty = 30
        
            self.speed = 2
        
        if type == 3:
            #Image
            self.image = pygame.Surface([70, 70])
            self.image.fill(OLIVE)
            self.rect = self.image.get_rect()
            #Parameters
            
            self.hp =800+50*wave
            self.basehp = self.hp
            self.score = 20000
            self.bounty = 100
            
        
            self.speed = 1
        
        self.goal = route[len(route)-1]
        
        self.current = 0
        
        self.rect.x = self.route[0][0]
        self.rect.y = self.route[0][1]
    
    #Enemy movement in the map
    def move(self):
        if self.current+1<len(self.route)-1:
            
            #X to rigth
            if self.route[self.current][0] < self.route[self.current+1][0]:
                self.rect.x += 1*self.speed
                
                if abs(self.rect.x-self.route[self.current+1][0])<7:
                    self.current += 1
            #X to left
            if self.route[self.current][0] > self.route[self.current+1][0]: 
                self.rect.x -= 1*self.speed
                    
                if abs(self.rect.x-self.route[self.current+1][0])<7:
                    self.current += 1
            #Y down
            if self.route[self.current][1] < self.route[self.current+1][1]:
                self.rect.y += 1*self.speed   
                
                if abs(self.rect.y-self.route[self.current+1][1])<7:
                    self.current += 1
            #Y up
            if self.route[self.current][1] > self.route[self.current+1][1]:
                self.rect.y -= 1*self.speed   
                
                if abs(self.rect.y-self.route[self.current+1][1])<7:
                    self.current += 1
                    
        #Last piece of road
        if self.current+1==len(self.route)-1:
            if self.route[self.current][0]<self.route[self.current+1][0]:
                self.rect.x += 1*self.speed
        
            if self.route[self.current][0] > self.route[self.current+1][0]:
                self.rect.x -= 1*self.speed
            
            if self.route[self.current][1] < self.route[self.current+1][1]:
                self.rect.y += 1*self.speed 
            
            if self.route[self.current][1] > self.route[self.current+1][1]:
                self.rect.y -= 1*self.speed  
        
        
        
  
    #Enemy update
    def update(self):
        #If enemy reaches goal
        if self.rect.x > 975 or self.rect.y > 975:
            player.hp -= 1
            player.score -= 4000
            player.killcount += 1
            self.kill()
            enemylist.remove(self)
        
        #Kill enemy
        if self.hp <=0:
            player.score += self.score
            player.money += self.bounty
            player.killcount += 1
            self.kill()
            enemylist.remove(self)
            
        self.move()
        
    