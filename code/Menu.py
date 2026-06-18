from code.Const import C_BLUE, C_RED, C_WHITE, C_YELLOW, MENU_OPTION, WIN_HEIGHT, WIN_WIDTH

import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/img/bg/menuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.logo = pygame.image.load("assets/img/ui/logo.png").convert_alpha()
        self.logo_rect = self.logo.get_rect(center=(WIN_WIDTH / 2, 100))

    def run(self, clock):
        # index da opção do menu
        menu_option = 0
        # musica
        pygame.mixer_music.load("./assets/music/bgm/Menu.ogg")
        pygame.mixer_music.play(-1)

        while True:
            # desenha img na tela
            self.window.blit(source=self.surf, dest=self.rect)
            self.window.blit(source=self.logo, dest=self.logo_rect)

            for i in range(len(MENU_OPTION)):
                # Se for a opção selecionada fica azul, senão fica vermelho (cores da logo)
                if i == menu_option:
                    self.menu_text(
                        16, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i)
                    )
                else:
                    self.menu_text(
                        16, MENU_OPTION[i], C_BLUE, ((WIN_WIDTH / 2), 200 + 25 * i)
                    )
            
            #Instruções de como jogar:
            self.menu_text(10, 'Setas: Cima/Baixo | Enter: Selecionar', C_WHITE, ((WIN_WIDTH / 2), WIN_HEIGHT - 40))
            self.menu_text(10, 'No Jogo: Esquerda/Direita - Mover  | Espaço - Correr', C_WHITE, ((WIN_WIDTH / 2), WIN_HEIGHT - 20))

            pygame.display.flip()
            clock.tick(60)

            # checa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha janela
                    quit()  # encerra pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # down key
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # up key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option < len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: #Return é o enter padrão e kp_enter é o enter do tec numérico
                        return MENU_OPTION[menu_option]
                    if event.key == pygame.K_ESCAPE: #ESC
                        pygame.quit()  # fecha janela
                        quit()  # encerra pygame

    # Função para setar texto do menu, pesquisei para colocar uma fonte específica já salva na pasta raiz para não depender do sistema.
    def menu_text(
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
