from code.Const import ENTITY_HEALTH, GAME_HEIGHT
from code.Entity import Entity
from code.Meat import Meat
from code.Meteor import Meteor
from code.Player import Player

import pygame


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Meteor, Meat)):
            if ent.rect.bottom >= GAME_HEIGHT:
                ent.health = 0
   
    @staticmethod
    def __verify_collision_entity(ent1, ent2, dmg_sfx, pwrUp_sfx):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, (Meteor, Meat)):
            valid_interaction = True
        elif isinstance(ent1, (Meteor, Meat)) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # se a interação for válida
            if (
                ent1.rect.right >= ent2.rect.left
                and ent1.rect.left <= ent2.rect.right
                and ent1.rect.bottom >= ent2.rect.top
                and ent1.rect.top <= ent2.rect.bottom
            ):
                if isinstance(ent1, Meteor) or isinstance(ent2, Meteor):
                    ent1.health -= ent2.damage
                    ent2.health -= ent1.damage
                    ent1.score += ent2.score
                    ent2.score += ent1.score
                    if isinstance(ent1, Meteor):
                        ent2.hurt_timer = 30
                    else:
                        ent1.hurt_timer = 30
                    pygame.mixer.Sound.play(dmg_sfx)

                if isinstance(ent1, Meat) or isinstance(ent2, Meat):
                    ent2.health -= ent1.damage
                    ent1.health -= ent2.damage
                    # condição para travar a soma de vidas até 3
                    # mesmo estando genérico a carne nunca terá vida 3 então sempre sofrerá dano
                    if isinstance(ent1, Player):
                        ent1.health = min(ent1.health, ENTITY_HEALTH[ent1.name])
                        ent1.score += ent2.score
                        ent1.hurt_timer = 0  # animação de hurt não dispara
                    if isinstance(ent2, Player):
                        ent2.health = min(ent2.health, ENTITY_HEALTH[ent2.name])
                        ent2.score += ent1.score
                        ent2.hurt_timer = 0  # animação de hurt não dispara
                    pygame.mixer.Sound.play(pwrUp_sfx)

    

    @staticmethod
    def verify_collision(entity_list: list[Entity], dmg_sfx, pwrUp_sfx):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(
                    entity1, entity2, dmg_sfx, pwrUp_sfx
                )

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
