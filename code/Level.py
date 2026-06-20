import random
import sys
from code.Const import (
    C_WHITE,
    EVENT_MEAT,
    EVENT_METEOR,
    EVENT_SCORE_TIME,
    EVENT_TIMEOUT,
    SCORE_TIME,
    SPAWN_MEAT_TIME,
    SPAWN_METEOR_TIME,
    TIMEOUT_LEVEL,
    TIMEOUT_STEP,
    WIN_HEIGHT,
    WIN_WIDTH,
)
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player

import pygame


class Level:
    def __init__(self, window):
        self.window = window
        # controles de tempo de score e fase
        self.score_time = SCORE_TIME
        self.timeout = TIMEOUT_LEVEL

        self.entity_list: list[Entity] = []
        self.bg = pygame.image.load(
            "./assets/img/bg/Background.png"
        )  # bg estático, então não foi criada uma classe específica
        self.bg_rect = self.bg.get_rect(left=0, top=0)
        self.heart = pygame.image.load("./assets/img/ui/heart.png")

        original_width = self.heart.get_width()
        original_height = self.heart.get_height()
        new_width = original_width * 2
        new_height = original_height * 2
        self.heart = pygame.transform.scale(self.heart, (new_width, new_height))

        # cria o player
        player = EntityFactory.get_entity("Player", (WIN_WIDTH / 2, 260))
        self.entity_list.append(player)
        # puxar sfx de colisões
        self.dmg_sfx = pygame.mixer.Sound("./assets/music/sfx/Hit.wav")
        self.pwrUp_sfx = pygame.mixer.Sound("./assets/music/sfx/Powerup.wav")

        # eventos de tempo
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
        pygame.time.set_timer(EVENT_METEOR, SPAWN_METEOR_TIME)
        pygame.time.set_timer(EVENT_MEAT, SPAWN_MEAT_TIME)
        pygame.time.set_timer(EVENT_SCORE_TIME, SCORE_TIME)

    def run(self, clock):
        # musica
        pygame.mixer_music.load("./assets/music/bgm/Fase.ogg")
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            # Pinta o bg
            self.window.blit(source=self.bg, dest=self.bg_rect)
            # Atualiza entidades
            for ent in self.entity_list:
                self.window.blit(ent.image, ent.rect)
                ent.update()
                # Mostrar quantidade de vida (POR ENQUANTO TESTE)
                if ent.name == "Player":
                    for i in range(ent.health):
                        pos_x = 20 + (i * 40)
                        pos_y = 20

                        self.window.blit(self.heart, (pos_x, pos_y))
                     
                    self.level_text(
                        14,
                        f"Tempo: {self.timeout / 1000:.1f}s | Score: {ent.score}",
                        C_WHITE,
                        ((WIN_WIDTH / 2) + 100, 30),
                    )

            for event in pygame.event.get():
                # controla o evento da queda do meteoro aleatoriamente, spawna ele e salva na lista de entidades
                if event.type == EVENT_METEOR:
                    position = random.randint(0, WIN_WIDTH)
                    meteoro = EntityFactory.get_entity("Meteor", (position, -50))
                    self.entity_list.append(meteoro)
                # evento da queda da carne, mesma lógica do meteoro
                if event.type == EVENT_MEAT:
                    position = random.randint(0, WIN_WIDTH)
                    meat = EntityFactory.get_entity("Meat", (position, -50))
                    self.entity_list.append(meat)
                if (
                    event.type == EVENT_SCORE_TIME
                ):  # cada vez que o tempo passar aumenta o score
                    for ent in self.entity_list:
                        if ent.name == "Player":
                            ent.score += 50
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        print("voce venceu")
                        return True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # condição para sabermos quando o jogador morre e terminar o jogo
                player_alive = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        player_alive = True
                if not player_alive:
                    print("game over")
                    return False

            # Texto fps e entidades na tela(testes)            
            self.level_text(
                12, f"fps: {clock.get_fps():.0f}", C_WHITE, (60, WIN_HEIGHT - 30)
            )
            # self.level_text(
            #     14,
            #     f"entidades: {len(self.entity_list)}",
            #     C_WHITE,
            #     (100, WIN_HEIGHT - 15),
            # )
            pygame.display.flip()
            # Teste de colisão (por enquanto meteoro sair da tela)
            EntityMediator.verify_collision(
                entity_list=self.entity_list,
                dmg_sfx=self.dmg_sfx,
                pwrUp_sfx=self.pwrUp_sfx,
            )
            EntityMediator.verify_health(entity_list=self.entity_list)

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
