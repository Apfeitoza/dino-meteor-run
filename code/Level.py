import random
import sys

from code.Const import (
    C_WHITE,
    EVENT_MEAT,
    EVENT_METEOR,
    SPAWN_METEOR_TIME,
    SPAWN_MEAT_TIME,
    WIN_HEIGHT,
    WIN_WIDTH,
)
from code.Entity import Entity
from code.EntityFactory import EntityFactory

import pygame

from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window):
        self.window = window
        self.entity_list: list[Entity] = []
        self.bg = pygame.image.load(
            "./assets/img/bg/Background.png"
        )  # bg estático, então não foi criada uma classe específica
        self.bg_rect = self.bg.get_rect(left=0, top=0)
        self.player = EntityFactory.get_entity("Player", (WIN_WIDTH / 2, 260))
        self.entity_list.append(self.player)

        pygame.time.set_timer(EVENT_METEOR, SPAWN_METEOR_TIME)
        pygame.time.set_timer(EVENT_MEAT, SPAWN_MEAT_TIME)

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

            for event in pygame.event.get():
                #controla o evento da queda do meteoro aleatoriamente, spawna ele e salva na lista de entidades
                if event.type == EVENT_METEOR:
                    position = random.randint(0, WIN_WIDTH)
                    meteoro = EntityFactory.get_entity("Meteor", (position, -50))
                    self.entity_list.append(meteoro)
                # evento da queda da carne, mesma lógica do meteoro
                if event.type == EVENT_MEAT:
                    position = random.randint(0, WIN_WIDTH)
                    meat = EntityFactory.get_entity("Meat", (position, -50))
                    self.entity_list.append(meat)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Texto fps e entidades na tela(testes)
            self.level_text(
                14, f"fps: {clock.get_fps():.0f}", C_WHITE, (60, WIN_HEIGHT - 30)
            )
            self.level_text(
                14,
                f"entidades: {len(self.entity_list)}",
                C_WHITE,
                (100, WIN_HEIGHT - 15),
            )
            pygame.display.flip()
            # Teste de colisão (por enquanto meteoro sair da tela)
            EntityMediator.verify_collision(entity_list=self.entity_list)
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
