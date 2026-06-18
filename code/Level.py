import sys
from code.Const import WIN_WIDTH
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

    def run(self):
        # musica
        pygame.mixer_music.load("./assets/music/bgm/Fase.ogg")
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        while True:
            # Pinta o bg
            self.window.blit(source=self.bg, dest=self.bg_rect)
            # Insere o P1
            self.player.update()
            self.window.blit(self.player.image, self.player.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
