import pygame
from setup import *


class Gamemap():
    
    def __init__ (self, width, height,road):
        self.grid = [None] * width
        self.road = road
        
        for x in range(self.get_width()):   
            self.grid[x] = [None] * height
            for y in range(self.get_height()):    
                self.grid[x][y] = 'O'
        
    #Check is position is free
    def can_build(self,coordinates):
        i = coordinates[0]
        j =coordinates[1]
        if self.grid[i][j] == 'O':
            return True
        else:
            return False
    #Add tower to map
    def build_tower(self,coordinates):
        i = coordinates[0]
        j =coordinates[1]
        self.grid[i][j] = 'T'
    
    #Creates route from road coordinates
    def create_route(self):
        route = [];
        
        i = 0
        while i < len(self.road)-1:
            if self.road[i][0] != self.road[i+1][0]:
                #First part of the road in x-axis if x-part is first
                if i==0:
                    y = self.road[i][1]
                    x1 = self.road[i][0]
                    x2 = self.road[i+1][0]
                    if x2-x1<0:
                        sign = -1
                    else:
                        sign = 1
                    for x in range(abs(x2-x1)+1):
                        if self.grid[sign*x][y] is not 'R':
                            self.grid[sign*x][y] = 'R'
                            route.append((sign*x,y))
                #Other parts in x-axis
                else:
                    y = self.road[i][1]
                    b = self.road[i][0]
                    x1 = self.road[i][0]
                    x2 = self.road[i+1][0]
                    if x2-x1<0:
                        sign = -1
                    else:
                        sign = 1
                    for x in range(abs(x2-x1)+1):
                        if self.grid[sign*x+b][y] is not 'R':
                            self.grid[sign*x+b][y] = 'R'
                            route.append((sign*x+b,y))
            
            if self.road[i][1] != self.road[i+1][1]: 
                    #First part of the road in y-axis if y-part is first
                    if i==0:
                        x = self.road[i][0]
                        y1 = self.road[i][1]
                        y2 = self.road[i+1][1]
                        if y2-y1<0:
                            sign = -1
                        else:
                            sign = 1
                        for y in range(abs(y2-y1)+1):
                            if self.grid[x][sign*y] is not 'R':
                                self.grid[x][sign*y] = 'R'
                                route.append((x,sign*y))
                    #Others parts of the road in y-axis
                    else:
                        x = self.road[i][0]
                        b = self.road[i][1]
                        y1 = self.road[i][1]
                        y2 = self.road[i+1][1]
                        if y2-y1<0:
                            sign = -1
                        else:
                            sign = 1
                        for y in range(abs(y2-y1)+1):
                            if self.grid[x][b+sign*y] is not 'R':
                                self.grid[x][b+sign*y] = 'R'
                                route.append((x,b+sign*y))
                        
            i += 1
    
        return route
    
    
    def scale_road(self):
        route = []
        for i in self.road:
            if i[0] == 0:
                x = 0
                y = i[1]*100+25
            elif i[1] == 0:
                x = i[0]*100+25
                y = 0
            else:
                x = i[0]*100+25
                y = i[1]*100+25
            route.append((x,y))
        return route
    def get_width(self):
        return len(self.grid)
    
    def get_height(self):
        return len(self.grid[0])
    
    
    def draw_road(self,road):
        i=0 
            #Draw map
        while i< len(road)-1:
            x1 = road[i][0]
            y1 = road[i][1]
            x2 = road[i+1][0]
            y2 = road[i+1][1]
                
            
            #First x-block
            if y1 == y2 and i == 0:
                pygame.draw.line(screen, BROWN, [x1,y1*100+50], [x2*100+100,y2*100+50], 100)  
            #X-blocks to rigth
            elif y1 == y2 and i>0 and x1-x2<0:
                pygame.draw.line(screen, BROWN, [x1*100,y1*100+50], [x2*100+100,y2*100+50], 100)
            #X-blocks to left
            elif y1 == y2 and i>0 and x1-x2>0:
                pygame.draw.line(screen, BROWN, [x1*100+100,y1*100+50], [x2*100,y2*100+50], 100)
            #Y-blocks 
            
            if x1 == x2 and i == 0:
                pygame.draw.line(screen, BROWN, [x1*100+50,y1*100], [x2*100+50,y2*100+100], 100)
                
            elif (x1 == x2 and i>0):  
                pygame.draw.line(screen, BROWN, [x1*100+50,y1*100+100], [x2*100+50,y2*100+100], 100)
                
            
            
                    
            i += 1 
            #Draw grid
            j = 0
            a = 0
            while j < 1000:
                while a < 1000:
                    pygame.draw.rect(screen, BLACK, [j, a, 100, 100], 1)
                    a = a+100
                a = 0
                j = j+100

    
        