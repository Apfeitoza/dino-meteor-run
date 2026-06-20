import sys
from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Level import Level
from code.Menu import Menu

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run(self.clock)

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window)
                level_return = level.run(self.clock)              
               
            elif menu_return == MENU_OPTION[1]:
                print("pontuação")
                pygame.quit()
                quit()
            elif menu_return == MENU_OPTION[2]:              
                pygame.quit()
                sys.exit()
