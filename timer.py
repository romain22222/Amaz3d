import pygame
from constantes import *

class Timer():
    def __Init__(self):
        self.fpsClock = pygame.time.Clock()
        self.TpsZero = pygame.time.get_ticks() ## Départ

    def temps(self):
        seconds = (pygame.time.get_ticks() - self.TpsZero) / 1000
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
