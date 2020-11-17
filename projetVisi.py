import sys, time, pygame
from joueur import *
from constantes import *
from labyrinthe import *
# https://fr.wikibooks.org/wiki/Pygame/Version_imprimable
# https://www.pygame.org/docs/ref/key.html#pygame.key.name
# https://github.com/TheAwesomePossum/StartPy/blob/3d6c824259fdf4e9e78e3138d2c9c0fecedf645f/Events.py
# https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

pygame.init()

screen = pygame.display.set_mode(size)

perso = pygame.image.load("perso.gif")
perso = pygame.transform.rotozoom(perso, 0, sizePlayer)
''' on divise la taille du personnage par 4 et on le tourne de 0 degre'''
persovar = perso.get_rect()         
persovar = persovar.move([posInitPlayerX,posInitPlayerY])
pygame.key.set_repeat(60, 60)

grids=createCubicLaby(tailleLabyCube)

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        persovar=movejoueur(persovar)
        

    screen.fill(BLACK)
    
    layerToPrint=1 #vise à changer dans le futur afin de progresser dans le laby
    printNeighbLabysCubicLaby(grids,screen,layerToPrint)

    screen.blit(perso, persovar)

    pygame.display.flip()
