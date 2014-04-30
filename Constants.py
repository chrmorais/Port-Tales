
""" Module defining useful constants """
import os

# GLOBAL RESSOURCES
ICON_FILE = "icon.png"
INSTRUCTION_FILE = "explication.png"
ENDSCREEN_FILE = "game_ended.png"
CREDITS_FILE = "credits.png"
GAMEOVER_FILE = "game_over.png"

# COLOR
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
GREY = 128,128,128
PURPLE = 255,0,255
YELLOW = 255,255,0
BACKGROUND_COLOR = 40, 30, 50

# WINDOW
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
REDUCE_FACTOR = 0.9
Y_OFFSET = -70
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT
WINDOW_TITLE = "Port Tales"
FULLSCREEN = False
NOFRAME = False

# LEVEL
NB_LEVELS = 8

# FONT
FONT_NAME = "advanced_led_board.ttf"
FONT_COLOR = 220,0,0
FONT_SIZE = 100
FONT_POS = 200,100

# TIME
FIRST_INSTRUCTION_TIME = 0
INSTRUCTION_TIME = -1
STAGE_TIME = 2
GAMEOVER_TIME = 2
ENDSCREEN_TIME = -1
CREDITS_TIME = -1

# SPRITES
SPRITE_WIDTH = 100

# IMAGE
IMG_FORMAT = "{:04}.png"

# MAP
MAP_DIR = "maps"
MAP_FILE = "map{}.txt"
MAP_FORMAT = os.path.join(MAP_DIR, MAP_FILE)

# SOUND
MUSIC_FILE = "son/puzz.wav"

# FPS
FPS = 30

