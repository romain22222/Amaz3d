import pygame
import random
from math import *

from constantes import *
class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hidden = False
        self.neighbors = []
        self.visited = False
        self.walls = [True, True, True, True]
        self.typeCase = "end"
        self.distsTo = {"start":0,"end":0}
        self.locked=False
        self.objects=[]
        
    def show(self, screen, wr, hr, leftTopCornerX, leftTopCornerY, color=BLACK):
        if self.hidden:
            pygame.draw.line(screen, ORANGE, [self.x*hr+leftTopCornerX, self.y*wr+leftTopCornerY],       [self.x*hr+hr+leftTopCornerX, self.y*wr+leftTopCornerY], 2)
            pygame.draw.line(screen, ORANGE, [self.x*hr+hr+leftTopCornerX, self.y*wr+leftTopCornerY],    [self.x*hr+hr+leftTopCornerX, self.y*wr + wr+leftTopCornerY], 2)
            pygame.draw.line(screen, ORANGE, [self.x*hr+hr+leftTopCornerX, self.y*wr+wr+leftTopCornerY], [self.x*hr+leftTopCornerX, self.y*wr+wr+leftTopCornerY], 2)
            pygame.draw.line(screen, ORANGE, [self.x*hr+leftTopCornerX, self.y*wr+wr+leftTopCornerY],    [self.x*hr+leftTopCornerX, self.y*wr+leftTopCornerY], 2)
        else:
            if self.walls[0]:
                pygame.draw.line(screen, color, [self.x*hr+leftTopCornerX, self.y*wr+leftTopCornerY],       [self.x*hr+hr+leftTopCornerX, self.y*wr+leftTopCornerY], 2)
            if self.walls[1]:
                pygame.draw.line(screen, color, [self.x*hr+hr+leftTopCornerX, self.y*wr+leftTopCornerY],    [self.x*hr+hr+leftTopCornerX, self.y*wr + wr+leftTopCornerY], 2)
            if self.walls[2]:
                pygame.draw.line(screen, color, [self.x*hr+hr+leftTopCornerX, self.y*wr+wr+leftTopCornerY], [self.x*hr+leftTopCornerX, self.y*wr+wr+leftTopCornerY], 2)
            if self.walls[3]:
                pygame.draw.line(screen, color, [self.x*hr+leftTopCornerX, self.y*wr+wr+leftTopCornerY],    [self.x*hr+leftTopCornerX, self.y*wr+leftTopCornerY], 2)

    def show_block(self, screen, wr, hr, leftTopCornerX, leftTopCornerY, color):
        if self.hidden:
            pygame.draw.rect(screen, ORANGE, [self.x*hr+2+leftTopCornerX, self.y*wr+2+leftTopCornerY, hr-2, wr-2])
        else:
            pygame.draw.rect(screen, color, [self.x*hr+2+leftTopCornerX, self.y*wr+2+leftTopCornerY, hr-2, wr-2])

    def add_neighbors(self, rows, cols, grid):
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.x < rows - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.y < cols - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
def createLaby(layer, rows = 6, cols = 6, gridInitPosCol= 0, gridInitPosRow = 0):
    #gridInitPosCol = int(random.random()*cols)
    #gridInitPosRow = int(random.random()*rows)
    pygame.init()
    done = False
    grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            grid[i][j].add_neighbors(rows, cols, grid)

    current = grid[gridInitPosCol][gridInitPosRow]
    visited = [current]
    completed = False

    def breakwalls(a, b):
        if a.y == b.y and a.x > b.x:
            grid[b.x][b.y].walls[1] = False
            grid[a.x][a.y].walls[3] = False
        if a.y == b.y and a.x < b.x:
            grid[a.x][a.y].walls[1] = False
            grid[b.x][b.y].walls[3] = False
        if a.x == b.x and a.y < b.y:
            grid[b.x][b.y].walls[0] = False
            grid[a.x][a.y].walls[2] = False
        if a.x == b.x and a.y > b.y:
            grid[a.x][a.y].walls[0] = False
            grid[b.x][b.y].walls[2] = False
    while not completed:
        grid[current.x][current.y].visited = True
        got_new = False
        temp = 22

        while not got_new and not completed:
            r = random.randint(0, len(current.neighbors)-1)
            Tempcurrent = current.neighbors[r]
            if not Tempcurrent.visited:
                visited.append(current)
                current = Tempcurrent
                got_new = True
            if temp == 0:
                temp = 22
                if len(visited) == 0:
                    completed = True
                else:
                    current = visited.pop()
                    for neighb in current.neighbors:
                        if not neighb=="end":
                            current.typeCase="path"
            temp = temp - 1

        if not completed:
            breakwalls(current, visited[len(visited)-1])
        current.visited = True
    grid[gridInitPosCol][gridInitPosRow].typeCase="init"
    ends=addEntreeSortie(grid, layer)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y].typeCase=="nextup" or grid[x][y].typeCase=="final":
                caseEnd=grid[x][y]
                caseInit=grid[gridInitPosCol][gridInitPosRow]
                done=True
                break
        if done:
            break
    neighbChecking(grid)
    addDistsTo(grid,caseInit,caseEnd)
    generateDoorNKey(grid,ends)
    return [grid,[caseInit,caseEnd],ends]

def printLaby(grid, screen, rows = 6, cols = 6, leftTopCornerX = 0, leftTopCornerY = 0, widthPcnt = 0.3, heightPcnt = 0.4):
    wr = widthPcnt*width/cols
    hr = heightPcnt*height/rows
    for i in range(rows):
        for j in range(cols):
            grid[i][j].show(screen, wr, hr, leftTopCornerX, leftTopCornerY, WHITE)
            if grid[i][j].typeCase=="end":
                grid[i][j].show_block(screen, wr, hr, leftTopCornerX, leftTopCornerY, BLUE)
            elif grid[i][j].typeCase=="start":
                grid[i][j].show_block(screen, wr, hr, leftTopCornerX, leftTopCornerY, GREEN)
            elif grid[i][j].typeCase=="nextup":
                grid[i][j].show_block(screen, wr, hr, leftTopCornerX, leftTopCornerY, LIGHTGRAY)
            elif grid[i][j].typeCase=="nextdown":
                grid[i][j].show_block(screen, wr, hr, leftTopCornerX, leftTopCornerY, DARKGRAY)
            elif grid[i][j].typeCase=="final":
                grid[i][j].show_block(screen, wr, hr, leftTopCornerX, leftTopCornerY, RED)
            else:
                grid[i][j].show_block(screen, wr, hr, leftTopCornerX, leftTopCornerY, BLACK)
            if grid[i][j].locked:
                grid[i][j].show_block(screen, wr, hr, leftTopCornerX, leftTopCornerY, (152,54,87))
            if "key" in grid[i][j].objects:
                grid[i][j].show_block(screen, wr, hr, leftTopCornerX, leftTopCornerY, (0,54,87))

def neighbChecking(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            newNeighb=[]
            for neighb in range(len(grid[x][y].walls)):
                if not grid[x][y].walls[neighb]:
                    if neighb==0:
                        newNeighb.append(grid[x][y-1])
                    elif neighb==1:
                        newNeighb.append(grid[x+1][y])
                    elif neighb==2:
                        newNeighb.append(grid[x][y+1])
                    else:
                        newNeighb.append(grid[x-1][y])
            grid[x][y].neighbors=newNeighb

def addDistsTo(grid,caseInit,caseEnd):
    addDistancesTo(grid, "start", caseInit)
    addDistancesTo(grid, "end", caseEnd)

def addDistancesTo(grid, typeDistance, caseDebut):
    grid[caseDebut.x][caseDebut.y].distsTo[typeDistance]=-1
    valDist=1
    neighbToCheck=grid[caseDebut.x][caseDebut.y].neighbors
    neighbToCheckNext=[]
    while len(neighbToCheck) != 0:
        for neighb in neighbToCheck:
            if neighb.distsTo[typeDistance]==0:
                neighb.distsTo[typeDistance]=valDist
                neighbToCheckNext=neighbToCheckNext+neighb.neighbors
        neighbToCheck=neighbToCheckNext
        neighbToCheckNext=[]
        valDist+=1
    grid[caseDebut.x][caseDebut.y].distsTo["start"]=0
    
def printLabyGrayScale(grid, screen, distToPrint="start", rows = 6, cols = 6, leftTopCornerX = 0, leftTopCornerY = 0, widthPcnt = 0.3, heightPcnt = 0.4):
    wr = widthPcnt*width/cols
    hr = heightPcnt*height/rows
    for i in range(rows):
        for j in range(cols):
            grid[i][j].show(screen, wr, hr, leftTopCornerX, leftTopCornerY, BLUE)
            valGray=int(255/sqrt(2*grid[i][j].distsTo[distToPrint]+1))
            grid[i][j].show_block(screen, wr, hr, leftTopCornerX, leftTopCornerY, (valGray,valGray,valGray))



def addEntreeSortie(grid, layer):
    ends=[]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].typeCase=="end":
                ends.append(grid[i][j])
            if grid[i][j].typeCase=="init":
                initCase=grid[i][j]
    if layer<len(grid)-1:
        chosenCase=random.randint(0,len(ends)-1)
        ends[chosenCase].typeCase="nextup"
        ends.pop(chosenCase)
    else:
        chosenCase=random.randint(0,len(ends)-1)
        ends[chosenCase].typeCase="final"
        ends.pop(chosenCase)
    if layer!=0:
        initCase.typeCase="nextdown"
    else:
        initCase.typeCase="start"
    return ends
        
def createCubicLaby(size):
    grids=[]
    caseInit=Spot(random.randint(0,size-1),random.randint(0,size-1))
    for i in range(size):
        done=False
        grids.append(createLaby(i,size,size,caseInit.x,caseInit.y))
        caseInit=grids[i][1][1]
    return grids

def printNeighbLabysCubicLaby(grids, screen, layer):
    sizeLaby=len(grids)
    
    printLaby(grids[layer][0], screen, sizeLaby, sizeLaby, POSXCentralLaby, POSYCentralLaby, widthCentralLaby, heightCentralLaby)
    if layer!=0:
        printLaby(grids[layer-1][0], screen, sizeLaby, sizeLaby, POSXLeftLaby, POSYLeftLaby, widthLeftLaby, heightLeftLaby)
    if layer!=len(grids)-1:
        printLaby(grids[layer+1][0], screen, sizeLaby, sizeLaby, POSXRightLaby, POSYRightLaby, widthRightLaby, heightRightLaby)

def generateDoorNKey(grid,ends):
    done=False
    while not done:
        door=[random.randint(0,len(grid[0])-1),random.randint(0,len(grid[0])-1)]
        key=random.randint(0,len(ends)-1)
        while grid[door[0]][door[1]]==grid[ends[key].x][ends[key].y]:
            key=random.randint(0,len(ends)-1)
        if grid[door[0]][door[1]].distsTo["end"]==grid[ends[key].x][ends[key].y].distsTo["end"]:
            grid[door[0]][door[1]].locked=True
            grid[ends[key].x][ends[key].y].objects.append("key")
            done=True
        elif grid[door[0]][door[1]].distsTo["start"]>grid[ends[key].x][ends[key].y].distsTo["start"]:
            grid[door[0]][door[1]].locked=True
            grid[ends[key].x][ends[key].y].objects.append("key")
            done=True

