import sys, time, pygame
width = 1200
height = 800
def movejoueur(persovar):
    'on bouge le joueur'
    keys = pygame.key.get_pressed()
    " si la touche est appuyé et si on ne sort pas de la fenêtre"
    if keys[pygame.K_UP] and persovar[1]-10>0:
        bouger=persovar.move([0,-10])
    elif keys[pygame.K_DOWN] and persovar[1]+persovar[3]+10<height:
        bouger=persovar.move([0,10])
    elif keys[pygame.K_RIGHT] and persovar[0]+persovar[2]+10<width:
        bouger=persovar.move([10,0])
    elif keys[pygame.K_LEFT] and persovar[0]-10>0:
        bouger=persovar.move([-10,0])
    else:
        bouger=persovar.move([0,0])
    return bouger

    

