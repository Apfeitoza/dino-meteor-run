from code.Const import ENTITY_HEALTH, ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity

import pygame


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.idle_frames_right = []  # virado para a direita
        self.idle_frames_left = []  # frame espelhado
        # carrega imagens
        for i in range(1, 5):
            img_right = pygame.image.load(
                f"assets/img/dino/idle/idle_{i}.png"
            ).convert_alpha()
            img_left = pygame.transform.flip(img_right, True, False)

            self.idle_frames_right.append(img_right)
            self.idle_frames_left.append(img_left)

        self.current_frame = 0
        self.facing_right = True

        self.image = self.idle_frames_right[self.current_frame]
        self.rect = self.image.get_rect(midbottom=self.position)       

    def update(self):
        # teclas pressionadas
        pressed_key = pygame.key.get_pressed()
        dash_speed = self.speed
        # velocidade do dash dobrada com espaço (correr)
        if pressed_key[pygame.K_SPACE]:
            dash_speed = dash_speed * 2
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += dash_speed
            self.facing_right = True
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= dash_speed
            self.facing_right = False

        # animação dos frames
        self.current_frame += 0.05 #mais devagar para ficar mais natural a transição dos frames
        if self.current_frame >= len(self.idle_frames_right):
            self.current_frame = 0 #se chegar ao fim da lista volta para a primeira

        index_frame = int(self.current_frame)

        if self.facing_right: # se estiver virado para a direita puxa a primeira lista de frames
            self.image = self.idle_frames_right[index_frame]
        else: # se estiver virado para a esquerda puxa a segunda lisata
            self.image = self.idle_frames_left[index_frame]

        self.rect = self.image.get_rect(center=self.rect.center) #redesenha a box do frame