import sys
from code.Const import GAME_HEIGHT, GAME_WIDTH, MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Level import Level
from code.Menu import Menu
from code.MenuSelect import MenuSelect
from code.Score import Score

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.display_surface = pygame.Surface(size=(GAME_WIDTH, GAME_HEIGHT))

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            score = Score(self.display_surface)
            menu = Menu(self.display_surface)
            self.display_surface.fill((0, 0, 0))
            menu_return = menu.run(self.clock)

            if menu_return == MENU_OPTION[0]:
                character_menu = MenuSelect(self.display_surface)
                character_menu_return = character_menu.run(self.clock)
                level = Level(self.display_surface, character_menu_return, 0)
                level_return, final_score = level.run(self.clock)
                if level_return:
                    score.save(menu_return, final_score)
                else:
                    score.game_over()
            elif menu_return == MENU_OPTION[1]:
                score.show()
                for event in pygame.event.get():
                    if event.key == pygame.K_ESCAPE:  # ESC
                        pygame.quit()  # fecha janela
                        quit()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()

            window_size = self.window.get_size()

            scaled_surf = pygame.transform.scale(self.display_surface, window_size)
            self.window.blit(scaled_surf, (0, 0))
            pygame.display.flip()
