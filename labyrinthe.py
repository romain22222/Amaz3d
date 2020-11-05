import pygame
import random
from constantes import *
pygame.init()

done = False

cols = rows = 12

widthPcnt = 0.3
heightPcnt = 0.8
wr = widthPcnt*width/cols
hr = heightPcnt*height/rows

class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.visited = False
        self.walls = [True, True, True, True]
        
    def show(self, color=BLACK):
        if self.walls[0]:
            pygame.draw.line(screen, color, [self.x*hr, self.y*wr],       [self.x*hr+hr, self.y*wr], 2)
        if self.walls[1]:
            pygame.draw.line(screen, color, [self.x*hr+hr, self.y*wr],    [self.x*hr+hr, self.y*wr + wr], 2)
        if self.walls[2]:
            pygame.draw.line(screen, color, [self.x*hr+hr, self.y*wr+wr], [self.x*hr, self.y*wr+wr], 2)
        if self.walls[3]:
            pygame.draw.line(screen, color, [self.x*hr, self.y*wr+wr],    [self.x*hr, self.y*wr], 2)

    def show_block(self, color):
        if self.visited:
            pygame.draw.rect(screen, color, [self.x*hr+2, self.y*wr+2, hr-2, wr-2])

    def add_neighbors(self):
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.x < rows - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.y < cols - 1:
            self.neighbors.append(grid[self.x][self.y + 1])


grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        grid[i][j].add_neighbors()

gridInitCol = int(random.random()*cols)
gridInitRow = int(random.random()*rows)
current = grid[gridInitCol][gridInitRow]
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


screen.fill(BLACK)
if not completed:
    grid[current.x][current.y].visited = True
    got_new = False
    temp = 10

    while not got_new and not completed:
        r = random.randint(0, len(current.neighbors)-1)
        Tempcurrent = current.neighbors[r]
        if not Tempcurrent.visited:
            visited.append(current)
            current = Tempcurrent
            got_new = True
        if temp == 0:
            temp = 10
            if len(visited) == 0:
                completed = True
                break
            else:
                current = visited.pop()
        temp = temp - 1

    if not completed:
        breakwalls(current, visited[len(visited)-1])

    for i in range(rows):
        for j in range(cols):
            grid[i][j].show(WHITE)
            grid[i][j].show_block(BLACK)

    current.visited = True
    current.show_block(BLACK)
    pygame.display.flip()
