import time, pygame, ast
from joueur import *
from constantes import *
from labyrinthe import *
from timer import *

import pygame_menu

# https://fr.wikibooks.org/wiki/Pygame/Version_imprimable
# https://www.pygame.org/docs/ref/key.html#pygame.key.name
# https://github.com/TheAwesomePossum/StartPy/blob/3d6c824259fdf4e9e78e3138d2c9c0fecedf645f/Events.py
# https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed

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

def set_pseudo(value):
    with open('options.txt', 'r') as file:
        data = file.readlines()
    data[2] = value+'\n'
    with open('options.txt', 'w') as file:
        file.writelines(data)

def changeMenuHS():
    global tempTableHS
    with open('highscores.txt', 'r') as file:
        hs = file.read()
        hs = ast.literal_eval(hs)
    with open('options.txt', 'r') as file:
        opt = file.readlines()
    hsImportant=hs[opt[3][:-1]][opt[5][:-1]][opt[4][:-1]]
    tempTableHS = pygame_menu.Menu(800,1200,'Highscores',theme=themeLaby, columns=3, rows=len(hsImportant)+2,joystick_enabled=False)
    
    tempTableHS.add_label("Highscores",font_size=52,font_color=RED)
    for pos in hsImportant.keys():  
        tempTableHS.add_label(str(pos)+'.', font_size=40)
    tempTableHS.add_label('', font_size=52)
    
    tempTableHS.add_label(opt[5][:-1]+' '+opt[4][:-1],font_size=52)
    for couple in hsImportant.values():
        tempTableHS.add_label(couple[0], font_size=40)
    if len(hsImportant):
        tempTableHS.add_label('', font_size=52)
    else:
        tempTableHS.add_label('Pas de temps encore enregistre', font_size=20, font_color=(127,127,127,127))
    
    tempTableHS.add_label(opt[3][:-1],font_size=52)
    for couple in hsImportant.values():
        tempTableHS.add_label(couple[1], font_size=40)
    tempTableHS.add_button('Retour', menu)
    tempTableHS.mainloop(screen)

def set_type_hs(value,type):
    with open('options.txt', 'r') as file:
        data = file.readlines()
    data[3] = type+'\n'
    with open('options.txt', 'w') as file:
        file.writelines(data)

def set_difficulty_hs(value, difficulty):
    with open('options.txt', 'r') as file:
        data = file.readlines()
    data[4] = difficulty+'\n'
    with open('options.txt', 'w') as file:
        file.writelines(data)

def set_mode_hs(value, mode):
    with open('options.txt', 'r') as file:
        data = file.readlines()
    data[5] = mode+'\n'
    with open('options.txt', 'w') as file:
        file.writelines(data)


def start_the_game():
    difficultyChosen, MODESELECTED, TEMPSINIT, BOOSTTIMEREDUCE, tailleLabyCube=chargeParams()
    lapT,finalT=partie()
    with open('options.txt', 'r') as file:
        data = file.readlines()
    pseudo = data[2][:-1]
    checkHs('LAYER',MODESELECTED,difficultyChosen,lapT,pseudo)
    checkHs('TOTAL',MODESELECTED,difficultyChosen,finalT,pseudo)

def menu():
    set_difficulty('',"veryEasy")
    set_mode('',"Contre-la-montre")
    set_pseudo('Player')
    set_type_hs('','TOTAL')
    set_difficulty_hs('',"veryEasy")
    set_mode_hs('',"Contre-la-montre")

    menuHS = pygame_menu.Menu(800, 1200, 'Highscores',theme=themeLaby,joystick_enabled=False)
    menuHS.add_label("Highscores",font_size=96,font_color=RED)
    menuHS.add_vertical_margin(50)
    menuHS.add_selector('Type : ', [("TOTAL","TOTAL"),("LAYER","LAYER")], onchange=set_type_hs)
    menuHS.add_selector('Mode : ', [("Contre-la-montre","Contre-la-montre"),("Temps limite","Temps limite")], onchange=set_mode_hs)
    menuHS.add_selector('Difficulty : ', [("veryEasy","veryEasy"),("easy","easy"),("medium","medium"),("hard","hard"),("challenge","challenge")], onchange=set_difficulty_hs)
    menuHS.add_button('Afficher les highscores correspondants', changeMenuHS)
    menuHS.add_button('Retour', pygame_menu.events.BACK)

    menu = pygame_menu.Menu(800, 1200, 'Amaz3d',theme=themeLaby,joystick_enabled=False)
    menu.add_label("Amaz3d",font_size=96,font_color=RED)
    menu.add_vertical_margin(50)
    menu.add_text_input('Joueur : ', default=initPseudo, maxchar=13, valid_chars=validChars, onchange=set_pseudo)
    menu.add_selector('Difficulty : ', [("veryEasy","veryEasy"),("easy","easy"),("medium","medium"),("hard","hard"),("challenge","challenge")], onchange=set_difficulty)
    menu.add_selector('Mode : ', [("Contre-la-montre","Contre-la-montre"),("Temps limite","Temps limite")], onchange=set_mode)
    menu.add_button('Play', start_the_game)
    menu.add_button('Highscores', menuHS)
    menu.add_button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)



def partie():
    difficultyChosen, MODESELECTED, TEMPSINIT, BOOSTTIMEREDUCE, tailleLabyCube=chargeParams()
    grids=createCubicLaby(tailleLabyCube)
    perso = Joueur(grids[0][1][0])
    chrono=Timer()
    if MODESELECTED==2:
        chrono.isMode2=True
    else:
        chrono.isMode2=False
    chrono.TpsZero=pygame.time.get_ticks()
    chrono.fpsClock = pygame.time.Clock()
    layerToPrint=0
    chronoLap=Timer()
    chronoLap.TpsZero=pygame.time.get_ticks()
    chronoLap.fpsClock = pygame.time.Clock()
    chronoLap.isMode2=False
    while perso.onCase.typeCase!="final":
        lEv=[]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event not in lEv:
                layerToPrint2, chrono=perso.movejoueur(grids,layerToPrint,chrono)
                if layerToPrint != layerToPrint2:
                    if layerToPrint==0:
                        bestLap=chronoLap.temps()
                    elif bestLap>chronoLap.temps():
                        bestLap=chronoLap.temps()
                    chronoLap.TpsZero=pygame.time.get_ticks()
                    if MODESELECTED==2:
                        chrono.timeReduce(BOOSTTIMEREDUCE*1000)
                    layerToPrint=layerToPrint2
                    pygame.event.clear()
                lEv.append(event)
        screen.fill(BLACK)
        
        printNeighbLabysCubicLaby(grids,screen,layerToPrint)
        perso.printPerso(screen)

        chrono.print_timer(screen,myfont)
        perso.printInventory(screen)

        pygame.display.flip()
        chrono.fpsClock.tick(60)
        pygame.event.get()
        if MODESELECTED==2 and chrono.temps() <= 0:
            break;
        time.sleep(0.05)
    fTime=chrono.temps()
    if bestLap>pygame.time.get_ticks()-chronoLap.TpsZero:
        bestLap=pygame.time.get_ticks()-chronoLap.TpsZero
    
    screen.fill(BLACK)
    finalS = myfont.render("Well played !", False, RED)
    screen.blit(finalS,(490, 150))
    pygame.display.flip()
    time.sleep(1)
    finalS = myfont.render("Votre temps total : "+str(fTime), False, RED)
    screen.blit(finalS,(420, 300))
    pygame.display.flip()
    time.sleep(1)
    finalS = myfont.render("Votre meilleur temps sur un étage : "+str(bestLap), False, RED)
    screen.blit(finalS,(360, 450))
    pygame.display.flip()
    time.sleep(5)

    return bestLap, fTime

def checkHs(type,MODESELECTED,difficultyChosen,time,pseudo):
    with open('highscores.txt', 'r') as file:
        highscores = file.read()
        highscores = ast.literal_eval(highscores)
    place=1
    valueNew=(pseudo,time)
    if MODESELECTED==1:
        for values in highscores[type]['Contre-la-montre'][difficultyChosen].values():
            if values[1]>valueNew[1]:
                tempValNew=values
                highscores[type]['Contre-la-montre'][difficultyChosen][place]=valueNew
                valueNew=tempValNew
            place+=1
        highscores[type]['Contre-la-montre'][difficultyChosen][place]=valueNew
    elif MODESELECTED==2:
        for values in highscores[type]['Temps limite'][difficultyChosen].values():
            if values[1]<valueNew[1]:
                tempValNew=values
                values=valueNew
                valueNew=tempValNew
            place+=1
        highscores[type]['Temps limite'][difficultyChosen][place]=valueNew
    with open('highscores.txt', 'w') as file:
        file.write(str(highscores))


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
