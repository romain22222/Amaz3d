import sys, time, pygame
from constantes import *
from labyrinthe import *


class Joueur:
    def __init__(self,x,y,grid):
        self.onCase=grid[x][y]
        self.inventaire=[]
        self.sprite=pygame.image.load("Minion.png")
    
    def movejoueur(persovar):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] and not self.onCase.walls[0]:
            self.onCase=grid[x][y-1]
        elif keys[pygame.K_DOWN] and not self.onCase.walls[2]:
            self.onCase=grid[x][y+1]
        elif keys[pygame.K_RIGHT] and not self.onCase.walls[1]:
            self.onCase=grid[x+1][y]
        elif keys[pygame.K_LEFT] and not self.onCase.walls[3]:
            self.onCase=grid[x-1][y]
        else:
            self.onCase=grid[x][y]

    



