import sys
from code.Const import C_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.EntityFactory import EntityFactory

import pygame


class Level:
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load(
            "./assets/img/bg/Background.png"
        )  # bg estático, então não foi criada uma classe específica
        self.bg_rect = self.bg.get_rect(left=0, top=0)
        self.player = EntityFactory.get_entity("Player", (WIN_WIDTH / 2, 260))

    def run(self, clock):
        # musica
        pygame.mixer_music.load("./assets/music/bgm/Fase.ogg")
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            # Pinta o bg
            self.window.blit(source=self.bg, dest=self.bg_rect)
            # Insere o P1
            self.player.update()
            self.window.blit(self.player.image, self.player.rect)

            #texto fps(mexer depois)
            self.level_text(
                14, f"fps: {clock.get_fps():.0f}", C_WHITE, (60, WIN_HEIGHT - 25)
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            clock.tick(60)

            

    def level_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple
    ):
        text_font: pygame.Font = pygame.font.Font(
            "assets/font/PressStart2P-Regular.ttf", size=text_size
        )

        text_surf: pygame.Surface = text_font.render(
            text, True, text_color
        ).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
