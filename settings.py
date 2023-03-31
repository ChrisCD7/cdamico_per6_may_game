WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 1
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 0.25
MOB_FRICTION = -0.3
BLACK = (0,0,0)
BLUE = (50,50,255)
RED = (255,50,50)
WHITE = (255,255,255)
OFFWHITE = (250, 249, 246)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(150, 15, 200, 450, WHITE, "bouncy"),
                 (WIDTH, 50, 0, HEIGHT-50, (0,0,0), "normal"),
                 (150, 15, 100, 250, OFFWHITE, "disappaering"),
                 (150, 15, 550, 250, WHITE, "icy"),
                 (150, 15, 50, 50, WHITE, "normal")]