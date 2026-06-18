import sys
from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu
from code.Level import Level

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window)
                level_return = level.run()
                print("jogando")
                pygame.quit()
                quit()
            elif menu_return == MENU_OPTION[1]:
                print("pontuação")
                pygame.quit()
                quit()
            else:
                pygame.quit()
                sys.exit()
