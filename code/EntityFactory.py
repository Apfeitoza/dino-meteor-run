from code.Const import ENTITY_HEALTH
from code.Meat import Meat
from code.Meteor import Meteor
from code.Player_backup import Player

import pygame


class EntityFactory:
    # função para percorrer todos os nossos frames de animação dinamicamente
    @staticmethod
    def load_frames(
        base_path: str, num_frames: int, flip: bool = False, scale_size: tuple = None
    ):
        frames = []

        for i in range(
            1, num_frames + 1
        ):  # quantidade de frames + 1 para garantir que percorra todos os itens, começa em 0
            img = pygame.image.load(
                f"{base_path}{i}.png"
            ).convert_alpha()  # puxa dinamicamente o caminho da img

            # flipa a imagem
            if flip:
                img = pygame.transform.flip(img, True, False)

            # aumenta a escala da imagem
            if scale_size:
                img = pygame.transform.scale(img, scale_size)
            frames.append(img)  # faz o append dos frames na lista
        return frames

    @staticmethod
    def get_entity(entity_name: str, position: tuple, speed_multiplier=1):
        match entity_name:
            case "Doux" | "Mort" | "Tard" | "Vita":
                directory = entity_name.lower()
                # carrega todas as animações direto na factory através da função genérica
                player_animations = {
                    "idle_right": EntityFactory.load_frames(
                        f"assets/img/dino/{directory}/idle/idle_", 4, False
                    ),
                    "idle_left": EntityFactory.load_frames(
                        f"assets/img/dino/{directory}/idle/idle_", 4, True
                    ),
                    "move_right": EntityFactory.load_frames(
                        f"assets/img/dino/{directory}/move/move_", 6, False,
                    ),
                    "move_left": EntityFactory.load_frames(
                        f"assets/img/dino/{directory}/move/move_", 6, True 
                    ),
                    "sneak_right": EntityFactory.load_frames(
                        f"assets/img/dino/{directory}/sneak/sneak_", 7, False
                    ),
                    "sneak_left": EntityFactory.load_frames(
                        f"assets/img/dino/{directory}/sneak/sneak_", 7, True
                    ),
                    "hurt_right": EntityFactory.load_frames(
                        f"assets/img/dino/{directory}/hurt/hurt_", 4, False
                    ),
                    "hurt_left": EntityFactory.load_frames(
                        f"assets/img/dino/{directory}/hurt/hurt_", 4, True
                    ),
                }
                initial_health = ENTITY_HEALTH[entity_name]

                return Player(entity_name, position, player_animations, initial_health)

            case "Meteor":
                meteor_animations = {
                    "fall": EntityFactory.load_frames(
                        "assets/img/meteor/meteor_", 5, False
                    )
                }
                entity = Meteor(entity_name, position, meteor_animations)
                entity.speed *= speed_multiplier  # aplica o multiplicador de velocidade
                return entity
            case "Meat":
                # não tem animação então a gente só carrega a imagem aqui
                meat_frame = pygame.image.load("./assets/img/items/meat.png")
                # meat_frame_doubled = pygame.transform.scale(meat_frame, (52, 40))
                entity = Meat(entity_name, position, meat_frame)
                entity.speed *= speed_multiplier
                return entity
        pass
