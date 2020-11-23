import sys, time, pygame
from constantes import *
from labyrinthe import *


class Joueur:
    def __init__(self,case):
        self.onCase=case
        self.inventaire=[]
        self.sprite=pygame.image.load("Minion.png")
    
    def movejoueur(self,grids,layer):
        keys = pygame.key.get_pressed()
        x=self.onCase.x
        y=self.onCase.y
        if keys[pygame.K_UP] and not self.onCase.walls[0]:
            self.onCase=grids[layer][0][x][y-1]
        elif keys[pygame.K_DOWN] and not self.onCase.walls[2]:
            self.onCase=grids[layer][0][x][y+1]
        elif keys[pygame.K_RIGHT] and not self.onCase.walls[1]:
            self.onCase=grids[layer][0][x+1][y]
        elif keys[pygame.K_LEFT] and not self.onCase.walls[3]:
            self.onCase=grids[layer][0][x-1][y]
        else:
            self.onCase=grids[layer][0][x][y]
        print(self.onCase.x,self.onCase.y)
    



