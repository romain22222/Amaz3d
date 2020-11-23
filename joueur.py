import sys, time, pygame
from constantes import *
from labyrinthe import *


class Joueur:
    def __init__(self,case):
        wr = widthCentralLaby*width/tailleLabyCube
        hr = heightCentralLaby*height/tailleLabyCube
        self.onCase=case
        self.inventaire=[]
        self.sprite=pygame.transform.scale(pygame.image.load("Minion.png"),(int(hr)-4,int(wr)-4))
        self.cadre = self.sprite.get_rect()
        self.cadre = self.cadre.move([self.onCase.x*hr+3+POSXCentralLaby, self.onCase.y*wr+3+POSYCentralLaby])
        
    
    def movejoueur(self,grids,layer):
        keys = pygame.key.get_pressed()
        x=self.onCase.x
        y=self.onCase.y
        wr = widthCentralLaby*width/len(grids[layer][0])
        hr = heightCentralLaby*height/len(grids[layer][0][x])
        print("up", self.onCase.walls[0])
        print("down", self.onCase.walls[2])
        print("right", self.onCase.walls[1])
        print("left", self.onCase.walls[3])

        if keys[pygame.K_UP] and not self.onCase.walls[0]:
            self.onCase=grids[layer][0][x][y-1]
            self.cadre = self.cadre.move([0,-wr])
        elif keys[pygame.K_DOWN] and not self.onCase.walls[2]:
            self.onCase=grids[layer][0][x][y+1]
            self.cadre = self.cadre.move([0,wr])
        elif keys[pygame.K_RIGHT] and not self.onCase.walls[1]:
            self.onCase=grids[layer][0][x+1][y]
            self.cadre = self.cadre.move([hr,0])
        elif keys[pygame.K_LEFT] and not self.onCase.walls[3]:
            self.onCase=grids[layer][0][x-1][y]
            self.cadre = self.cadre.move([-hr,0])

    def printPerso(self, screen):
        screen.blit(self.sprite,self.cadre)
    



