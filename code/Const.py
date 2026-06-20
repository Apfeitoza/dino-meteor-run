# C
import pygame

C_BLUE = (29, 135, 248)
C_RED = (231, 81, 81)
C_WHITE = (255, 255, 255)
C_YELLOW = (231, 223, 65)

# E

ENTITY_HEALTH = {
    "Player": 3,
    "Meteor": 1,
    "Meat": 1,
}

ENTITY_SPEED = {
    "Player": 2,
    "Meteor": 1,
    "Meat": 1,
}

ENTITY_DAMAGE = {
    "Player": 1,
    "Meteor": 1,
    "Meat": -1,
}

ENTITY_SCORE = {
    "Meat": 100,
    "Meteor": 0,
    "Player": 0,
}

EVENT_METEOR = pygame.USEREVENT + 1
EVENT_MEAT = pygame.USEREVENT + 2
EVENT_SCORE_TIME = pygame.USEREVENT + 3
EVENT_TIMEOUT = pygame.USEREVENT + 4


# M
MENU_OPTION = ("NEW GAME", "SCORE", "EXIT")


# S
SPAWN_METEOR_TIME = 1500
SPAWN_MEAT_TIME = 6000
SCORE_TIME = 10000


# T
TIMEOUT_LEVEL = 15000  # 60s
TIMEOUT_STEP = 100  # 100ms

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {
    "Title": (WIN_WIDTH / 2, 50),
    "EnterName": (WIN_WIDTH / 2, 80),
    "Label": (WIN_WIDTH / 2, 90),
    "Name": (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}
