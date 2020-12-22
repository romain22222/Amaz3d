import time, pygame
from joueur import *
from constantes import *
from labyrinthe import *
from timer import *
# https://fr.wikibooks.org/wiki/Pygame/Version_imprimable
# https://www.pygame.org/docs/ref/key.html#pygame.key.name
# https://github.com/TheAwesomePossum/StartPy/blob/3d6c824259fdf4e9e78e3138d2c9c0fecedf645f/Events.py
# https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont('Comic Sans MS', 30)

pygame.key.set_repeat(60, 60)

grids=createCubicLaby(tailleLabyCube)

perso = Joueur(grids[0][1][0])

chrono=Timer()
chrono.TpsZero=pygame.time.get_ticks()
chrono.fpsClock = pygame.time.Clock()

layerToPrint=0



while perso.onCase.typeCase!="final":
    lEv=[]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event not in lEv:
            layerToPrint2, chrono=perso.movejoueur(grids,layerToPrint,chrono)
            if layerToPrint != layerToPrint2:
                if MODESELECTED==2:
                    chrono.timeReduce(BOOSTTIMEREDUCE*1000)
                layerToPrint=layerToPrint2
                pygame.event.clear()
            lEv.append(event)
    screen.fill(BLACK)
    
    printNeighbLabysCubicLaby(grids,screen,layerToPrint)
    perso.printPerso(screen)

    chrono.print_timer(screen,myfont)
     
    pygame.display.flip()
    chrono.fpsClock.tick(60)
    pygame.event.get()
    if MODESELECTED==2 and chrono.temps() <= 0:
        break;
    time.sleep(0.05)

print(chrono.convert_time())
