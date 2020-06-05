import pygame,os,sys,ast

class Player():
    def __init__(self):
        self.hp = 20
        self.startinghp = self.hp
        self.money = 500
        self.startingmoney = self.money
        self.wave = 1
        self.score = 0
        self.killcount = 0
        

    #Shows necessary game info
def show_game_info():
    font1 = pygame.font.SysFont("None", 40)
    font2 = pygame.font.SysFont("None", 35)
    font3 = pygame.font.SysFont("None", 20)
    font4 = pygame.font.SysFont("None", 55)
    
    life = font1.render("Lives: %d"% player.hp,1, (255,255,255))
    score = font1.render("Score: %d"% player.score,1, (255,255,255))
    money = font1.render("Money: %d"% player.money,1, (255,255,255))
    wave = font4.render("Wave: %d / %d"% (player.wave ,waves),1, (255,255,255))
    shop1 = font2.render("Shop",1, (0,0,0))
    shop2 = font3.render("Click the tower icon to buy",1, (0,0,0))
    info1 = font3.render("Mouseover tower and press 'U' to upgrade",1, (0,0,0))
    info2 = font3.render("Press 'R' to restart game",1, (0,0,0))
    info3 = font3.render("Press 'Esc' to quit game",1, (0,0,0))
    
    screen.blit(life,(1020,90))
    screen.blit(score,(1020,120))
    screen.blit(money,(1020,150))
    screen.blit(wave,(1020,20))
    screen.blit(shop1,(1100,230))
    screen.blit(shop2,(1050,260))
    screen.blit(info1, (1020,800))
    screen.blit(info2, (1020,825))
    screen.blit(info3, (1020,850))
    
#Reads textfile and converts it to datalist  
def read_file(filename):
    datalist = []
    road_found = False
    enemywaves_found = False
    try:
        file = open(filename)
        for line in file:      
            if 'road' in line:
                datalist.append(line[5:len(line)])
                s = datalist[0]
                road = eval(s)
                datalist[0] = road
                road_found = True
            
            if 'enemywaves' in line:
                datalist.append(line[11:len(line)])
                s = datalist[1]
                enemywaves = eval(s)
                datalist[1] = enemywaves
                enemywaves_found = True
    
        
        file.close()
    except OSError:
        print("Could not open file! Please give correct file.")

        

    if road_found is False or enemywaves_found is False:
        print("Correct datafile to the right format.")
        return
    return datalist






def enemy_count(enemywaves):
    count = 0
    for i in enemywaves:
        count += i[1]
    return count
    
    
#add player to the game
player = Player()

#lists that handles enemies and towers
enemylist = []
towerlist = []

#datalist reads a textfile and it contains gamemap, enemy waves etc.
datalist = read_file("datafile3.txt")
try:
    waves = len(datalist[1])
except TypeError:
    print("Correct datafile to the right format.")

#lists that handles sprites of enemies and towers
enemysprites = pygame.sprite.Group()
towersprites = pygame.sprite.Group()

#set screen and background
screen = pygame.display.set_mode((1300, 1000))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill ((0,0,0))
screen.blit(background, (0,0))

#define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (50,250,50)
GREEN2 = ( 0, 122,0)
BROWN =  (160,82,45)
RED = (255,0,0)
OLIVE = (107,142,35)
INDIGO = (75,0,130)
#tower colors
BLUE_TOWER = (30,144,255)
BLUE_TOWER2 = (0,139,139)
BLUE_TOWER3 = (34,0,255)
RED_TOWER = (250,65,65)
RED_TOWER2 = (238,36,36)
RED_TOWER3 = (254,0,255)
YELLOW_TOWER = (255,255,0)
YELLOW_TOWER2 = (255,230,0)
YELLOW_TOWER3 = (215,219,103)
