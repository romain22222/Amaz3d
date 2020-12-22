# la taille de la fenetre
size = width, height = 1200, 800

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKGRAY = (100,100,100)
LIGHTGRAY = (200,200,200)
ORANGE = (255,165,0)

# Positions et tailles labyrinthes sur écran

taillesLaby={"veryEasy":7,"easy":9,"medium":12,"hard":15,"challenge":20}
difficultyChosen="challenge"

tailleLabyCube=taillesLaby[difficultyChosen]

MODESELECT={"Contre-la-montre":1,"Temps limité":2}
MODESELECTED=MODESELECT["Temps limité"]

if MODESELECTED==2:
	timeTotal={"veryEasy":300,"easy":300,"medium":240,"hard":180,"challenge":120}
	TEMPSINIT=timeTotal[difficultyChosen]*1000

	BOOSTTIME = {"veryEasy":10,"easy":10,"medium":15,"hard":15,"challenge":15}
	BOOSTTIMEREDUCE = BOOSTTIME[difficultyChosen]


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
