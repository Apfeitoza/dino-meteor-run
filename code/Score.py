import sys
from code.Const import C_BLUE, C_RED, C_WHITE, C_YELLOW, MENU_OPTION, SCORE_POS
from code.DBProxy import DBProxy
from datetime import datetime

import pygame
from pygame import K_BACKSPACE, K_ESCAPE, K_RETURN, KEYDOWN, Rect, Surface
from pygame.font import Font


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load("./assets/img/bg/menuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load("./assets/music/bgm/Menu.ogg")
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy("DBScore")
        name = ""
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(32, "YOU WIN!!", C_RED, SCORE_POS["Title"])
            text = "Enter Player 1 name (4 characters):"
            score = player_score
            if game_mode == MENU_OPTION[0]:
                score = player_score

            self.score_text(14, text, C_WHITE, SCORE_POS["EnterName"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save(
                            {"name": name, "score": score, "date": get_formatted_date()}
                        )
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(14, name, C_WHITE, SCORE_POS["Name"])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load("./assets/music/bgm/Menu.ogg")
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(32, "TOP 10 SCORE", C_RED, SCORE_POS["Title"])
        self.score_text(
            12, "NAME     SCORE           DATE      ", C_YELLOW, SCORE_POS["Label"]
        )
        db_proxy = DBProxy("DBScore")
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(
                12,
                f"{name}     {score:05d}     {date}",
                C_YELLOW,
                SCORE_POS[list_score.index(player_score)],
            )
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple
    ):
        text_font: pygame.Font = pygame.font.Font(
            "assets/font/PressStart2P-Regular.ttf", size=text_size
        )
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
