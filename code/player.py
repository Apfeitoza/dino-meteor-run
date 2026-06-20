from code.Const import WIN_WIDTH
from code.Entity import Entity

import pygame


class Player(Entity):
    def __init__(self, name, position, animations):
        super().__init__(name, position, animations)

        self.state = "idle"
        self.current_frame = 0
        self.facing_right = True

        # puxando animações da Entity
        self.image = self.animations["idle_right"][0]
        self.rect = self.image.get_rect(midbottom=self.position)

    def update(self):
        # teclas pressionadas
        pressed_key = pygame.key.get_pressed()
        dash_speed = self.speed

        # velocidade do dash dobrada com espaço (correr)
        self.state = "idle"
        if pressed_key[pygame.K_SPACE]:
            dash_speed = dash_speed * 2
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += dash_speed
            if pressed_key[pygame.K_SPACE]:
                self.state = "sneak"
            else:
                self.state = "move"
            self.facing_right = True
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= dash_speed
            self.facing_right = False
            if pressed_key[pygame.K_SPACE]:
                self.state = "sneak"
            else:
                self.state = "move"

        # direção dos frames
        direction = "right" if self.facing_right else "left"
        animation_key = f"{self.state}_{direction}"
        frame_list = self.animations[animation_key]

        # animação dos frames
        self.current_frame += (
            0.15  # mais devagar para ficar mais natural a transição dos frames
        )
        if self.current_frame >= len(frame_list):
            self.current_frame = 0  # se chegar ao fim da lista volta para a primeira

        self.image = frame_list[int(self.current_frame)]   

        self.rect = self.image.get_rect(
            center=self.rect.center
        )  # redesenha a box do frame
