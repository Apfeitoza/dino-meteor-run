from code.Const import WIN_HEIGHT
from code.Entity import Entity
from code.Meat import Meat
from code.Meteor import Meteor


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Meteor):
            if ent.rect.bottom >= WIN_HEIGHT:
                ent.health = 0
        if isinstance(ent, Meat):
            if ent.rect.bottom >= WIN_HEIGHT:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            # for j in range(i + 1, len(entity_list)):
            #     entity2 = entity_list[j]
            #     EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, (Meteor, Meat)):
                    entity_list.remove(ent)
