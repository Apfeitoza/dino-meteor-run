import sys
import pygame


class Level:
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load(
            "./assets/img/bg/Background.png"
        )  # bg estático, então não foi criada uma classe específica
        self.bg_rect = self.bg.get_rect(left=0, top=0)

    def run(self):
        # musica
        pygame.mixer_music.load("./assets/music/bgm/Fase.ogg")
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.bg, dest=self.bg_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
