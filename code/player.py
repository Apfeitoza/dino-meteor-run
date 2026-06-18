from code.Const import PLAYER_ANIMATIONS, WIN_WIDTH
from code.Entity import Entity

import pygame


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.animations = PLAYER_ANIMATIONS 
        # carrega imagens idle        
        for i in range(1, 5):
            img = pygame.image.load(
                f"assets/img/dino/idle/idle_{i}.png"
            ).convert_alpha()
            self.animations["idle_right"].append(img)
            self.animations["idle_left"].append(pygame.transform.flip(img, True, False))
        # carrega imagens movimento
        for i in range(1, 7):
            img = pygame.image.load(
                f"assets/img/dino/move/move_{i}.png"
            ).convert_alpha()
            self.animations["move_right"].append(img)
            self.animations["move_left"].append(pygame.transform.flip(img, True, False))
        # carrega imagens corrida
        for i in range(1, 8):
            img = pygame.image.load(
                f"assets/img/dino/sneak/sneak_{i}.png"
            ).convert_alpha()
            self.animations["sneak_right"].append(img)
            self.animations["sneak_left"].append(pygame.transform.flip(img, True, False))
        # carrega colisão
        for i in range(1, 5):
            img = pygame.image.load(
                f"assets/img/dino/hurt/hurt_{i}.png"
            ).convert_alpha()
            self.animations["hurt_right"].append(img)
            self.animations["hurt_left"].append(pygame.transform.flip(img, True, False))

        self.state = "idle"
        self.current_frame = 0
        self.facing_right = True

        self.image = self.animations['idle_right'][0]
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
                self.state = 'sneak'
            else:
                self.state = 'move'
            self.facing_right = True
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= dash_speed
            self.facing_right = False
            if pressed_key[pygame.K_SPACE]:
                self.state = 'sneak'
            else:
                self.state = 'move'        

        #direção dos frames
        direction = 'right' if self.facing_right else 'left'
        animation_key = f'{self.state}_{direction}'
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
