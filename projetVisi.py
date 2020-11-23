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

#nouvelle instance de joueur
joueur = joueur()
       
#pygame.key.set_repeat(60, 60)

grids=createCubicLaby(tailleLabyCube)

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

# si une touche a ete pressee
        elif event.type == pygame.KEYDOWN:
            joueur.movejoueur(joueur)
           

    # on met l'arriere plan en noir, peut-etre par la suite une image en fonction des salles ?
        screen.fill(BLACK)

    # on met le joueur à sa position
        screen.blit(joueur.image, (joueur.rect))

    layerToPrint=1 #vise à changer dans le futur afin de progresser dans le laby
    printNeighbLabysCubicLaby(grids,screen,layerToPrint)

    

    pygame.display.flip()
