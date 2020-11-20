import sys, time, pygame
from constantes import * 

#on définit le joueur comme un sprite : un objet dans notre jeu
class joueur(pygame.sprite.Sprite):

# initialisation du joueur
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("perso.gif")
        #self.image = pygame.transform.rotozoom(self.image, 0, sizePlayer)
# on divise la taille du personnage par 4 et on le tourne de 0 degre
        self.rect = self.image.get_rect()
# on met notre joueur à la case d'entree (par la suite)
        self.rect.x= POSXCentralLaby
        self.rect.y= POSYCentralLaby

        self.hauteurcase = widthCentralLaby*100
        self.largeurcase = heightCentralLaby*150
        self.nbcletrouve=0

    def movejoueur(self, arg):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.y-10>0:
            self.rect.y= self.rect.y - self.hauteurcase
        elif keys[pygame.K_DOWN] and self.rect.y+self.rect[3]+10<height:
            self.rect.y= self.rect.y + self.hauteurcase
        elif keys[pygame.K_RIGHT] and self.rect.x+self.rect[3]+10<width:
            self.rect.x= self.rect.x + self.largeurcase
        elif keys[pygame.K_LEFT] and self.rect.x-10>0:
            self.rect.x= self.rect.x - self.largeurcase
        else:
            print('pas bouger')


    def movejoueurtoaposition (self, pos):
# pos sera un (x,y)
        self.rect.x= pos.x
        self.rect.y= pos.y


    def isCollision(self, laby):
        collision = pygame.sprite.collide_rect(laby)

        if collision==True:
            return True
        else:
            return False



