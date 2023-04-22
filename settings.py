WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 1
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 0.25
MOB_FRICTION = -0.3
MOB_JUMP = 20
BLACK = (0,0,0)
BLUE = (50,50,255)
RED = (255,50,50)
WHITE = (255,255,255)
OFFWHITE = (250, 249, 246)
YELLOW = (255, 255, 0)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(150, 15, 200, 450, WHITE, "bouncy"),
                 (WIDTH, 50, 0, HEIGHT-50, (0,0,0), "normal"),
                 (150, 15, 100, 250, YELLOW, "disappearing"),
                 (150, 15, 550, 250, WHITE, "icy"),
                 (150, 15, 50, 50, WHITE, "normal")]
                ##### Plane Bars #####
                #  (800, 15, 0, 0, BLUE, "pmob"),
                #  (800, 15, 0, 40, BLUE, "pmob"),
                #  (800, 15, 0, 80, BLUE, "pmob"),
                #  (800, 15, 0, 120, BLUE, "pmob"),
                #  (800, 15, 0, 160, BLUE, "pmob"),
                #  (800, 15, 0, 200, BLUE, "pmob"),
                #  (800, 15, 0, 240, BLUE, "pmob"),
                #  (800, 15, 0, 280, BLUE, "pmob"),
                #  (800, 15, 0, 320, BLUE, "pmob"),
                #  (800, 15, 0, 360, BLUE, "pmob"),
                #  (800, 15, 0, 400, BLUE, "pmob"),
                #  (800, 15, 0, 440, BLUE, "pmob"),
                #  (800, 15, 0, 480, BLUE, "pmob"),
                #  (800, 15, 0, 520, BLUE, "pmob")]