import pygame
from constantes import *

def chargeParams():
    with open('options.txt', 'r') as file:
        data = file.readlines()

    difficultyChosen = data[0][:-1]
    MODESELECTED=MODESELECT[data[1][:-1]]
    tailleLabyCube=taillesLaby[difficultyChosen]
    TEMPSINIT=timeTotal[difficultyChosen]*1000
    BOOSTTIMEREDUCE = BOOSTTIME[difficultyChosen]

    return difficultyChosen, MODESELECTED, TEMPSINIT, BOOSTTIMEREDUCE, tailleLabyCube

class Timer():
    def __Init__(self):
        self.fpsClock = pygame.time.Clock()
        self.TpsZero = pygame.time.get_ticks() ## Départ

    def temps(self):
        difficultyChosen, MODESELECTED, TEMPSINIT, BOOSTTIMEREDUCE, tailleLabyCube=chargeParams()
        if MODESELECTED==1:
            seconds = (pygame.time.get_ticks() - self.TpsZero) / 1000
        elif MODESELECTED==2:
            seconds = (self.TpsZero - pygame.time.get_ticks() + TEMPSINIT) / 1000
        return seconds

    def print_timer(self,screen,myfont):
        textsurface = myfont.render(self.convert_time(), False, RED)
        screen.blit(textsurface,(0.48*width,0.05*height))
        
    def convert_time(self):
        time=self.temps()
        minute=int(time//60)
        seconde=int(time%60)
        ms=int((time*1000)%1000)
        return "{:0>2}' {:0>2}\" {:0>3}".format(minute,seconde,ms)

    def timeReduce(self, t):
        if self.TpsZero+t<pygame.time.get_ticks():
            self.TpsZero+=t
        else:
            self.TpsZero=pygame.time.get_ticks()

