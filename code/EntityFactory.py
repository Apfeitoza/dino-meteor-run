from code.Meteor import Meteor
from code.Player import Player

import pygame


class EntityFactory:
    # função para percorrer todos os nossos frames de animação dinamicamente
    @staticmethod
    def load_frames(base_path: str, num_frames: int, flip: bool = False):
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

            frames.append(img)  # faz o append dos frames na lista
        return frames

    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case "Player":
                # carrega todas as animações direto na factory através da função genérica
                player_animations = {
                    "idle_right": EntityFactory.load_frames(
                        "assets/img/dino/idle/idle_", 4, False
                    ),
                    "idle_left": EntityFactory.load_frames(
                        "assets/img/dino/idle/idle_", 4, True
                    ),
                    "move_right": EntityFactory.load_frames(
                        "assets/img/dino/move/move_", 6, False
                    ),
                    "move_left": EntityFactory.load_frames(
                        "assets/img/dino/move/move_", 6, True
                    ),
                    "sneak_right": EntityFactory.load_frames(
                        "assets/img/dino/sneak/sneak_", 7, False
                    ),
                    "sneak_left": EntityFactory.load_frames(
                        "assets/img/dino/sneak/sneak_", 7, True
                    ),
                    "hurt_right": EntityFactory.load_frames(
                        "assets/img/dino/hurt/hurt_", 4, False
                    ),
                    "hurt_left": EntityFactory.load_frames(
                        "assets/img/dino/hurt/hurt_", 4, True
                    ),
                }
                return Player(entity_name, position, player_animations)
            case "Meteor":
                meteor_animations = {
                    "fall": EntityFactory.load_frames("assets/img/meteor/meteor_", 5, False)
                }
                return Meteor(entity_name, position, meteor_animations)
        pass
