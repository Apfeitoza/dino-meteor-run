# C
import pygame

C_BLUE = (29, 135, 248)
C_RED = (231, 81, 81)
C_WHITE = (255, 255, 255)
C_YELLOW = (231, 223, 65)

CHARACTER_OPTION = ("Doux", "Mort", "Tard", "Vita")
CHARACTER_DIR_SELECTION = ("doux", "mort", "tard", "vita")

# E

ENTITY_HEALTH = {
    "Doux": 3,
    "Mort": 1,
    "Tard": 2,
    "Vita": 5,
    "Meteor": 1,
    "IcyMeteor": 1,
    "Meat": 1,
}

ENTITY_SPEED = {
    "Doux": 2,
    "Mort": 4,
    "Tard": 3,
    "Vita": 1,
    "Meteor": 1,
    "IcyMeteor": 2,
    "Meat": 1,
}

ENTITY_DAMAGE = {
    "Doux": 1,
    "Mort": 1,
    "Tard": 1,
    "Vita": 1,
    "Meteor": 1,
    "IcyMeteor": 2,
    "Meat": -1,
}

ENTITY_SCORE = {
    "Meat": 100,
    "Meteor": 0,
    "IcyMeteor": -100,
    "Doux": 0,
    "Mort": 0,
    "Tard": 0,
    "Vita": 0,
}

EVENT_METEOR = pygame.USEREVENT + 1
EVENT_ICY_METEOR = pygame.USEREVENT + 5
EVENT_MEAT = pygame.USEREVENT + 2
EVENT_SCORE_TIME = pygame.USEREVENT + 3
EVENT_TIMEOUT = pygame.USEREVENT + 4

# G

GAME_WIDTH = 576
GAME_HEIGHT = 324


# M
MENU_OPTION = ("NEW GAME", "SCORE", "EXIT")


# S
SPAWN_METEOR_TIME = 1000
SPAWN_ICY_METEOR_TIME = 3000
SPAWN_MEAT_TIME = 4000
SCORE_TIME = 10000


# T
TIMEOUT_LEVEL = 60000  # 60s
TIMEOUT_STEP = 100  # 100ms

# W
WIN_WIDTH = 1152
WIN_HEIGHT = 648

# S
SCORE_POS = {
    "Title": (GAME_WIDTH / 2, 50),
    "EnterName": (GAME_WIDTH / 2, 80),
    "Label": (GAME_WIDTH / 2, 90),
    "Name": (GAME_WIDTH / 2, 110),
    0: (GAME_WIDTH / 2, 110),
    1: (GAME_WIDTH / 2, 130),
    2: (GAME_WIDTH / 2, 150),
    3: (GAME_WIDTH / 2, 170),
    4: (GAME_WIDTH / 2, 190),
    5: (GAME_WIDTH / 2, 210),
    6: (GAME_WIDTH / 2, 230),
    7: (GAME_WIDTH / 2, 250),
    8: (GAME_WIDTH / 2, 270),
    9: (GAME_WIDTH / 2, 290),
}

#VOLUME
SFX_VOLUME = 0.1
MUSIC_VOLUME = 0.2