import unittest
import pygame


from gamemap import *
from setup import *
from tower import *
from enemy import *


class TestGamemap(unittest.TestCase):

    def test_grid(self):
        road = [(0,3),(3,3),(3,7),(7,7),(7,4),(5,4),(5,1),(9,1)]
        map = Gamemap(10,10,road)
        self.assertEqual( map.grid[5][5],'O' , "Free position should be indicated by 'O'")
    
    def test_create_road1(self):
        road = [(0,3),(3,3),(3,7),(7,7),(7,4),(5,4),(5,1),(9,1)]
        map = Gamemap(10,10,road)
        occupied = [(0, 3), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (5, 3), (5, 2), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)]
        self.assertEqual(map.create_route(), occupied , "Routes are not same")

    def test_create_road2(self):
        road = [(0,5),(5,5),(5,9)]
        map = Gamemap(10,10,road)
        occupied = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)]
        self.assertEqual(map.create_route(), occupied , "Routes are not same")

    def test_road(self):
        road = [(0,5),(5,5),(5,9)]
        map = Gamemap(10,10,road)
        map.create_route()
        self.assertEqual( map.grid[5][5],'R' , "Road should be indicated by 'R'")
        
    def test_tower(self):
        road = [(0,5),(5,5),(5,9)]
        map = Gamemap(10,10,road)
        map.build_tower((5,4))
        self.assertEqual( map.grid[5][4],'T' , "Tower should be indicated by 'T'")
        
    
    def test_can_build1(self):
        road = [(0,3),(3,3),(3,7),(7,7),(7,4),(5,4),(5,1),(9,1)]
        map = Gamemap(10,10,road)
        self.assertEqual( map.can_build((0,0)),True , "Should be able to build tower")
    
    def test_can_build2(self):
        road = [(0,3),(3,3),(3,7),(7,7),(7,4),(5,4),(5,1),(9,1)]
        map = Gamemap(10,10,road)
        map.create_route()
        self.assertEqual( map.can_build((0,3)),False , "Should not be able to build tower to road")
        
     
    def test_add_tower1(self):
        road = [(0,3),(3,3),(3,7),(7,7),(7,4),(5,4),(5,1),(9,1)]
        map = Gamemap(10,10,road)
        map.build_tower((0,1))
        self.assertEqual( map.can_build((0,1)),False , "Should not be able to build tower on top of another tower")   
        
        
class TestSetup(unittest.TestCase):    
    
    def test_enemy_count1(self):
        enemywaves = [(1,5),(2,5),(1,10),(3,1),(2,10),(1,15),(2,20),(3,2),(1,25)]
        self.assertEqual(enemy_count(enemywaves), 93, "Count is not rigth")
    
    def test_enemy_count2(self):
        enemywaves = [(1,5),(2,5),(1,10),(3,1),(2,10)]
        self.assertNotEqual(enemy_count(enemywaves), 1, "Count is not rigth")

    def test_read_file1(self):
        datalist = read_file('datafile.txt')
        self.assertEqual(len(datalist), 2, "Wrong length")
        
    def test_read_file2(self):
        datalist = read_file('datafile.txt')
        rightdata = [[(0,3),(3,3),(3,7),(7,7),(7,4),(5,4),(5,1),(9,1)],[(1,5),(2,5),(1,10),(3,1),(2,10),(1,15),(2,20),(3,2),(1,25)]]
        self.assertEqual(datalist,rightdata , "Wrong data from the file")
        
    def test_read_file3(self):
        
        try:
            datalist = read_file('data.txt')
        except UnboundLocalError as error:
            check = error
            self.assertNotEqual(None, check, "Error in filename")
            
class TestTower(unittest.TestCase):
        
    
    def test_tower1(self):
        t1 = Tower(1,1,1)
        self.assertEqual(len(towerlist),2,"Tower was not added to towerlist")
    
    def test_tower2(self):
        t1 = Tower(1,1,1)
        t2 = Tower(1,2,1)
        t3 = Tower(1,3,1)
        self.assertEqual(len(towerlist),5,"Tower was not added to towerlist")
    
    def test_target(self):
        road = [(0,5),(5,5),(5,9)]
        map = Gamemap(10,10,road)
        route = map.create_route()
        enemy1 = Enemy(1,route,1)
        enemy2 = Enemy(1,route,1)
        tower = Tower(0,4,1)
        t = tower.target()
        self.assertEqual(t, (enemy1.rect.x,enemy1.rect.y), "Wrong target")
            

    def test_up(self):
        t1 = Tower(1,1,1)
        t1.up()
        self.assertEqual(t1.level, 2, "Unsuccesful upgrade ")
        t1.up()
        self.assertEqual(t1.level, 3, "Unsuccesful upgrade ")
        t1.up()
        self.assertNotEqual(t1.level, 4, "Unsuccesful upgrade ")
        

    


if __name__ == '__main__':
    unittest.main()