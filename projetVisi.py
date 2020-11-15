import sys, time, pygame
from joueur import *
from constantes import *
from labyrinthe import *
# https://fr.wikibooks.org/wiki/Pygame/Version_imprimable
# https://www.pygame.org/docs/ref/key.html#pygame.key.name
# https://github.com/TheAwesomePossum/StartPy/blob/3d6c824259fdf4e9e78e3138d2c9c0fecedf645f/Events.py
# https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

pygame.init()

black = 0, 0, 0

screen = pygame.display.set_mode(size)

perso = pygame.image.load("perso.gif")
perso = pygame.transform.rotozoom(perso, 0, 0.25)
''' on divise la taille du personnage par 4 et on le tourne de 0 degre'''
persovar = perso.get_rect()         
persovar = persovar.move([600,500])
pygame.key.set_repeat(60, 60)
tailleLabyCube=6
grids=[]
caseInit=[2,2]
for i in range(tailleLabyCube):
    done=False
    grids.append(createLaby(i,tailleLabyCube,tailleLabyCube,caseInit[0],caseInit[1]))
    for x in range(len(grids[i])):
        for y in range(len(grids[i][x])):
            if grids[i][x][y].typeCase=="nextup":
                caseInit=[grids[i][x][y].x,grids[i][x][y].y]
                done=True
                break
        if done:
            break

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        persovar=movejoueur(persovar)
        

    screen.fill(black)
    X=0
    Y=0
    for grid in grids:
        printLaby(grid, screen, tailleLabyCube, tailleLabyCube, X, Y, 0.2, 0.2)
        X+=200
    screen.blit(perso, persovar)

    time.sleep(0.01)

    pygame.display.flip()
