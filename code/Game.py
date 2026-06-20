import sys
from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run(self.clock)

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, menu_return, 0)
                level_return, final_score = level.run(self.clock)
                if level_return:
                    score.save(menu_return, final_score)
            elif menu_return == MENU_OPTION[1]:
                score.show()
                for event in pygame.event.get():
                    if event.key == pygame.K_ESCAPE:  # ESC
                        pygame.quit()  # fecha janela
                        quit()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()
