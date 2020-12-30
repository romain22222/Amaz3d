import time, pygame
from joueur import *
from constantes import *
from labyrinthe import *
from timer import *

import pygame_menu

# https://fr.wikibooks.org/wiki/Pygame/Version_imprimable
# https://www.pygame.org/docs/ref/key.html#pygame.key.name
# https://github.com/TheAwesomePossum/StartPy/blob/3d6c824259fdf4e9e78e3138d2c9c0fecedf645f/Events.py
# https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont('Comic Sans MS', 30)

pygame.key.set_repeat(60, 60)

def set_difficulty(value, difficulty):
    with open('options.txt', 'r') as file:
        data = file.readlines()
    data[0] = difficulty+'\n'
    with open('options.txt', 'w') as file:
        file.writelines(data)

def set_mode(value, mode):
    with open('options.txt', 'r') as file:
        data = file.readlines()
    data[1] = mode+'\n'
    with open('options.txt', 'w') as file:
        file.writelines(data)

def start_the_game():
    difficultyChosen, MODESELECTED, TEMPSINIT, BOOSTTIMEREDUCE, tailleLabyCube=chargeParams()
    finalT=partie()


def menu():

    menu = pygame_menu.Menu(800, 1200, 'Amaz3d',
                           theme=pygame_menu.themes.THEME_BLUE)

    menu.add_text_input('Joueur :', default='')
    menu.add_selector('Difficulty :', [("veryEasy","veryEasy"),("easy","easy"),("medium","medium"),("hard","hard"),("challenge","challenge")], onchange=set_difficulty)
    menu.add_selector('Mode :', [("Contre-la-montre","Contre-la-montre"),("Temps limité","Temps limité")], onchange=set_mode)
    menu.add_button('Play', start_the_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

def partie():
    difficultyChosen, MODESELECTED, TEMPSINIT, BOOSTTIMEREDUCE, tailleLabyCube=chargeParams()
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

    return chrono.temps()

set_difficulty('',"veryEasy")
set_mode('',"Contre-la-montre")

def chargeParams():
    with open('options.txt', 'r') as file:
        data = file.readlines()

    difficultyChosen = data[0][:-1]
    MODESELECTED=MODESELECT[data[1][:-1]]
    tailleLabyCube=taillesLaby[difficultyChosen]
    TEMPSINIT=timeTotal[difficultyChosen]*1000
    BOOSTTIMEREDUCE = BOOSTTIME[difficultyChosen]

    return difficultyChosen, MODESELECTED, TEMPSINIT, BOOSTTIMEREDUCE, tailleLabyCube
menu()