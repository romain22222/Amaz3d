import pygame_menu
import pygame
import string

# la taille de la fenetre
size = width, height = 1200, 800

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKGRAY = (100,100,100)
DDGRAY = (50,50,50)
LIGHTGRAY = (200,200,200)
LLGRAY=(225,225,225)
ORANGE = (255,165,0)

# Dictionnaires des difficultés et modes

taillesLaby={"veryEasy":8,"easy":10,"medium":13,"hard":16,"challenge":20}
MODESELECT={"Contre-la-montre":1,"Temps limite":2}

timeTotal={"veryEasy":300,"easy":300,"medium":240,"hard":180,"challenge":120}
BOOSTTIME = {"veryEasy":10,"easy":10,"medium":15,"hard":15,"challenge":15}

# Positions et tailles labyrinthes sur écran

POSXLeftLaby=150
POSYLeftLaby=200
widthLeftLaby=0.3
heightLeftLaby=0.3

POSXCentralLaby=450
POSYCentralLaby=150
widthCentralLaby=0.4
heightCentralLaby=0.4

POSXRightLaby=820
POSYRightLaby=200
widthRightLaby=0.3
heightRightLaby=0.3

# Thème des menus

themeLaby = pygame_menu.themes.THEME_DARK.copy()
themeLaby.background_color=BLACK
themeLaby.title_shadow=True
themeLaby.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL
themeLaby.widget_font=pygame_menu.font.FONT_MUNRO
themeLaby.title_offset=(460,175)
themeLaby.title_background_color=BLACK
themeLaby.title_font=pygame_menu.font.FONT_MUNRO
themeLaby.title_font_size=96
themeLaby.title_font_color=RED
themeLaby.scrollbar_color=RED
themeLaby.menubar_close_button=False

# Sprites et cadres des inventaires

spriteKeys = pygame.transform.scale(pygame.image.load("cle.jpg"),(30,50))
cadreKeys = spriteKeys.get_rect()
cadreKeys = cadreKeys.move([450, 700])

spriteWb = pygame.transform.scale(pygame.image.load("wall breaker.jpg"),(30,50))
cadreWb = spriteWb.get_rect()
cadreWb = cadreWb.move([650, 700])

#Police en jeu
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


# Constantes sur le pseudo

initPseudo='Player'
temp=(string.ascii_letters+string.digits+'!#$%&()*+-./:;<=>?@[]^_`{|}~')[0:]
validChars=[] 
validChars[:0]=temp