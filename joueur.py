import sys, time, pygame
from constantes import *
from labyrinthe import *
from timer import *


class Joueur:
    def __init__(self,case):
        wr = widthCentralLaby*width/tailleLabyCube
        hr = heightCentralLaby*height/tailleLabyCube
        self.onCase=case
        self.inventaire=[]
        self.sprite=pygame.transform.scale(pygame.image.load("Minion.png"),(int(hr)-4,int(wr)-4))
        self.cadre = self.sprite.get_rect()
        self.cadre = self.cadre.move([self.onCase.x*hr+3+POSXCentralLaby, self.onCase.y*wr+3+POSYCentralLaby])
        
    
    def movejoueur(self,grids,layer,timer):
        keys = pygame.key.get_pressed()
        x=self.onCase.x
        y=self.onCase.y
        wr = widthCentralLaby*width/len(grids[layer][0])
        hr = heightCentralLaby*height/len(grids[layer][0][x])
        
        def aMove(xplus,yplus):
            if not grids[layer][0][x+xplus][y+yplus].locked:
                self.onCase=grids[layer][0][x+xplus][y+yplus]
                self.cadre = self.cadre.move([xplus*hr,yplus*wr])
            elif "key" in self.inventaire:
                self.inventaire.remove("key")
                grids[layer][0][x+xplus][y+yplus].locked=False

        if keys[pygame.K_UP] and not self.onCase.walls[0]:
            aMove(0,-1)
        elif keys[pygame.K_DOWN] and not self.onCase.walls[2]:
            aMove(0,1)
        elif keys[pygame.K_RIGHT] and not self.onCase.walls[1]:
            aMove(1,0)
        elif keys[pygame.K_LEFT] and not self.onCase.walls[3]:
            aMove(-1,0)
        else:
            self.onCase=grids[layer][0][x][y]

        if self.onCase.typeCase=="nextup":
            layer+=1
        for obj in self.onCase.objects[:]:
            if "key"==obj:
                self.inventaire.append("key")
                self.onCase.objects.remove("key")
            elif "timer"==obj[:5]:
                timer.timeReduce(int(obj[-2:])*1000)
                self.onCase.objects.remove(obj)
        return layer, timer

    def printPerso(self, screen):
        screen.blit(self.sprite,self.cadre)
    



