import sys
from code.Const import (
    C_BLUE,
    C_RED,
    C_WHITE,
    C_YELLOW,
    CHARACTER_DIR_SELECTION,
    CHARACTER_OPTION,
    GAME_HEIGHT,
    GAME_WIDTH,
)
from code.EntityFactory import EntityFactory

import pygame


class MenuSelect:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/img/bg/menuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, clock):
        # index da opção do menu
        character_option = 0
        # contador dos frames das animações do dino
        frame_counter = 0
        # musica
        pygame.mixer_music.load("./assets/music/bgm/Menu.ogg")
        pygame.mixer_music.play(-1)
        # coloca imagem dos dinos na tela (ajustar para mostrar animação do idle)
        dino_animations = []

        for dino in CHARACTER_DIR_SELECTION:
            dino_frames = EntityFactory.load_frames(
                f"assets/img/dino/{dino}/idle/idle_", 4
            )
            frames_aumentados = [
                pygame.transform.scale(img, (44, 36)) for img in dino_frames
            ]
            dino_animations.append(frames_aumentados)

        while True:
            # desenha img na tela
            self.window.blit(source=self.surf, dest=self.rect)

            # controle das animações dos dinossauros
            frame_counter += 0.15

            if frame_counter >= 4:
                frame_counter = 0

            for i in range(4):
                actual_frame = int(frame_counter)
                place_frame = dino_animations[i][actual_frame]

                pos_x = (GAME_WIDTH / 2 - 177) + 105 * i

                self.window.blit(place_frame, (pos_x, (GAME_HEIGHT / 2) - 30))

            # desenha o titulo
            self.character_menu_text(
                32,
                "SELECT YOUR CHAR",
                C_RED,
                (GAME_WIDTH / 2, 50),
            )

            for i in range(len(CHARACTER_OPTION)):
                # Se for a opção selecionada fica azul, senão fica vermelho (cores da logo)
                if i == character_option:
                    self.character_menu_text(
                        16,
                        CHARACTER_OPTION[i],
                        C_YELLOW,
                        ((GAME_WIDTH / 2 - 165) + 110 * i, (GAME_HEIGHT / 2) + 30),
                    )
                    if CHARACTER_OPTION[i] == "Doux":
                        self.character_menu_text(
                            12,
                            "Health: Normal | Spd: Normal",
                            C_WHITE,
                            ((GAME_WIDTH / 2), (GAME_HEIGHT / 2) + 60),
                        )
                    if CHARACTER_OPTION[i] == "Mort":
                        self.character_menu_text(
                            12,
                            "Health: Very Low | Spd: Very Quick",
                            C_WHITE,
                            ((GAME_WIDTH / 2), (GAME_HEIGHT / 2) + 60),
                        )
                    if CHARACTER_OPTION[i] == "Tard":
                        self.character_menu_text(
                            12,
                            "Health: Low | Spd: Quick",
                            C_WHITE,
                            ((GAME_WIDTH / 2), (GAME_HEIGHT / 2) + 60),
                        )
                    if CHARACTER_OPTION[i] == "Vita":
                        self.character_menu_text(
                            12,
                            "Health: Very High | Spd: Slow",
                            C_WHITE,
                            ((GAME_WIDTH / 2), (GAME_HEIGHT / 2) + 60),
                        )
                else:
                    self.character_menu_text(
                        16,
                        CHARACTER_OPTION[i],
                        C_BLUE,
                        ((GAME_WIDTH / 2 - 165) + 110 * i, (GAME_HEIGHT / 2) + 30),
                    )

            # Instruções de como jogar:
            self.character_menu_text(
                10,
                "Arrows(Menu): Left/Right | Space/Enter: Select",
                C_WHITE,
                ((GAME_WIDTH / 2), GAME_HEIGHT - 40),
            )

            window_real = pygame.display.get_surface()
            scaled_surf = pygame.transform.scale(self.window, window_real.get_size())
            window_real.blit(scaled_surf, (0, 0))

            pygame.display.flip()
            clock.tick(60)

            # checa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha janela
                    sys.exit() # encerra pygame

                # teoricamente vai selecionar entre os dinos
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if character_option < len(CHARACTER_OPTION) - 1:
                            character_option += 1
                        else:
                            character_option = 0
                    if event.key == pygame.K_LEFT:
                        if character_option > 0:
                            character_option -= 1
                        else:
                            character_option = len(CHARACTER_OPTION) - 1
                    if event.key in (
                        pygame.K_RETURN,
                        pygame.K_KP_ENTER,
                        pygame.K_SPACE,
                    ):
                        return CHARACTER_OPTION[character_option]

                    if event.key == pygame.K_ESCAPE:  # ESC
                        pygame.quit()  # fecha janela
                        sys.exit()  # encerra pygame

    # Função para setar texto do menu, pesquisei para colocar uma fonte específica já salva na pasta raiz para não depender do sistema.
    def character_menu_text(
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
